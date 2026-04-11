"""
P3157 [CQOI2011] 动态逆序对
https://www.luogu.com.cn/problem/P3157

刪除一個元素 x 時，會消失的逆序對滿足：
1. y 在 x 左側，且 y > x，del_time(y) > del_time(x)
2. y 在 x 右側，且 y < x，del_time(y) > del_time(x)

這兩者都是三維偏序問題，可以使用 CDQ 分治解決。
"""

from itertools import accumulate

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

    def add(self, k: int, x: int) -> None:
        while k < len(self.tree):
            self.tree[k] += x
            k += k & -k

    def preSum(self, k: int) -> int:
        res = 0
        while k > 0:
            res += self.tree[k]
            k -= k & -k
        return res

    def query(self, l: int, r: int) -> int:
        if l > r:
            return 0
        return self.preSum(r) - self.preSum(l - 1)


def solve():
    n, m = map(int, input().split())
    A = [int(input()) for _ in range(n)]
    assert len(A) == n

    pos = [0] * (n + 1)  # 位置
    for i, v in enumerate(A, start=1):
        pos[v] = i

    out = [m + 1] * (n + 1)  # 被刪除的時間
    for t in range(1, m + 1):
        v = int(input())
        out[v] = t

    # 計算初始逆序對數
    bit = BIT(n + 2)
    ans = 0
    for v in A:
        ans += bit.query(v + 1, n)
        bit.add(v, 1)

    # 每次刪除的減少量
    diff = [0] * m
    diff[0] = ans

    # 每個元素的 (pos, val, del_time)
    data = [(i, v, out[v]) for i, v in enumerate(A, start=1)]

    # 執行一次 CDQ（左貢獻或右貢獻）
    def do(is_left: bool):
        items = [None] * n
        for idx, (p, v, t) in enumerate(data):
            if is_left:
                # 1. 左貢獻：pos(y) < pos(x) 且 val(y) > val(x) 且 del_time(y) > del_time(x)
                # 將 val 取反，統一為 val'(y) < val'(x)
                v = -v
            else:
                # 2. 右貢獻：pos(y) > pos(x) 且 val(y) < val(x) 且 del_time(y) > del_time(x)
                # 將 pos 取反，統一為 pos'(y) < pos'(x)
                p = -p
            items[idx] = (p, v, t, idx)
        items.sort(key=lambda x: x[0])  # 按 pos 排序

        # f[idx] 表示刪除下標為 idx 的元素後，會消失的逆序對數量
        f = [0] * n
        bit = BIT(m + 2)

        def cdq(left: int, right: int) -> None:
            if left == right:
                return
            mid = (left + right) // 2
            cdq(left, mid)
            cdq(mid + 1, right)

            i = left
            for j in range(mid + 1, right + 1):
                _, b, c, idx = items[j]
                while i <= mid and items[i][1] <= b:
                    bit.add(items[i][2], 1)
                    i += 1
                f[idx] += bit.query(c + 1, m + 2)

            # 恢復 BIT 的狀態
            for j in range(left, i):
                bit.add(items[j][2], -1)

            # 按照 val 排序
            items[left : right + 1] = sorted(
                items[left : right + 1], key=lambda x: x[1]
            )

        cdq(0, n - 1)

        # 把每個元素的貢獻累加到對應刪除時間
        for idx, (_, _, t) in enumerate(data):
            if t < m:
                diff[t] -= f[idx]

    # 左貢獻 + 右貢獻
    do(True)
    do(False)

    # 輸出每次刪除後的逆序對數量
    print(*list(accumulate(diff)), sep="\n")


if __name__ == "__main__":
    solve()
