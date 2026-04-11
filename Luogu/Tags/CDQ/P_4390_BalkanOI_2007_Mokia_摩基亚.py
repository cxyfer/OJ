"""
P4390 [BalkanOI 2007] Mokia 摩基亚
https://www.luogu.com.cn/problem/P4390

首先用二維前綴和的方式理解，令 f(i, j) 表示以 (i, j) 為右下角的矩形內的點的個數，
則左上角為 (a, b)，右下角為 (c, d) 的矩形內的點的個數為 f(c, d) - f(a - 1, d) - f(c, b - 1) + f(a - 1, b - 1)
自此可以把每條詢問拆解成四個詢問。

考慮第 i 個詢問，則等同於求 t(j) <= t(i) 且 x(j) <= x(i) 且 y(j) <= y(i) 的權重和，
這是一個三維偏序問題，可以使用 CDQ 分治解決。
"""

# fmt: off
import sys
it = iter(sys.stdin.read().splitlines())
def input():
    return next(it)
def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)) + end)
# fmt: on


class BIT:  # PURQ, 1-based
    __slots__ = ["tree"]

    def __init__(self, n: int):
        self.tree = [0] * (n + 1)

    def add(self, k: int, x: int) -> None:  # 令 nums[k] += x
        while k < len(self.tree):
            self.tree[k] += x
            k += k & -k

    def preSum(self, k: int) -> int:  # 求 nums[:k+1] 之和
        res = 0
        while k > 0:
            res += self.tree[k]
            k -= k & -k
        return res

    def query(self, l: int, r: int) -> int:  # 求 nums[l:r+1] 之和
        if l > r:
            return 0
        return self.preSum(r) - self.preSum(l - 1)


def solve():
    _, w = map(int, input().split())

    events = []
    ts = qid = 0
    while True:
        op, *args = map(int, input().split())
        if op == 3:
            break
        if op == 1:
            x, y, v = args
            events.append((ts, op, x, y, v))
        elif op == 2:
            x1, y1, x2, y2 = args
            events.append((ts, op, x1 - 1, y1 - 1, qid, 1))
            events.append((ts, op, x1 - 1, y2, qid, -1))
            events.append((ts, op, x2, y1 - 1, qid, -1))
            events.append((ts, op, x2, y2, qid, 1))
            qid += 1
        else:
            break
        ts += 1

    events.sort(key=lambda x: (x[0], x[2]))

    ans = [0] * qid
    bit = BIT(w + 1)
    tmp = [None] * len(events)

    def cdq(left: int, right: int) -> None:
        if left >= right:
            return
        mid = (left + right) // 2
        cdq(left, mid)
        cdq(mid + 1, right)

        i = left
        for j in range(mid + 1, right + 1):
            op, x, y = events[j][1], events[j][2], events[j][3]
            while i <= mid and events[i][2] <= x:
                if events[i][1] == 1:
                    bit.add(events[i][3], events[i][4])
                i += 1
            if op == 2:
                qid = events[j][4]
                factor = events[j][5]
                ans[qid] += bit.query(1, y) * factor

        # 恢復 BIT 的狀態
        for j in range(left, i):
            op, y, val = events[j][1], events[j][3], events[j][4]
            if op == 1:
                bit.add(y, -val)

        # 按照 x 排序
        # events[left : right + 1] = sorted(
        #     events[left : right + 1], key=lambda x: (x[2], x[1])
        # )
        i, j, k = left, mid + 1, left
        while i <= mid and j <= right:
            if events[i][2] <= events[j][2] or (events[i][2] == events[j][2] and events[i][1] <= events[j][1]):
                tmp[k] = events[i]
                i += 1
            else:
                tmp[k] = events[j]
                j += 1
            k += 1
        while i <= mid:
            tmp[k] = events[i]
            i += 1
            k += 1
        while j <= right:
            tmp[k] = events[j]
            j += 1
            k += 1
        for i in range(left, right + 1):
            events[i] = tmp[i]

    cdq(0, len(events) - 1)
    print(*ans, sep="\n")


if __name__ == "__main__":
    solve()
