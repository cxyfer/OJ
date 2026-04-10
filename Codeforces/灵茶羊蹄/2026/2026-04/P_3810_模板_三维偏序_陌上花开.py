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
    n, m = map(int, input().split())
    items = []
    for i in range(n):
        a, b, c = map(int, input().split())
        items.append((a, b, c, i))
    assert len(items) == n
    items.sort()

    # f[i] 表示滿足 a[j] <= a[i], b[j] <= b[i], c[j] <= c[i] 的 j 的個數
    f = [0] * n
    bit = BIT(m + 1)

    # 修正 (a, b, c) 相同時，只能統計到左側偏序元素的問題
    i = 0
    while i < n:
        st = i
        a, b, c, _ = items[i]
        while (
            i + 1 < n
            and items[i + 1][0] == a
            and items[i + 1][1] == b
            and items[i + 1][2] == c
        ):
            i += 1
        for j in range(st, i + 1):
            f[items[j][3]] = i - j
        i += 1

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
            f[idx] += bit.query(1, c)

        # 恢復 BIT 的狀態
        for j in range(left, i):
            bit.add(items[j][2], -1)

        # 按照 b 排序
        items[left : right + 1] = sorted(items[left : right + 1], key=lambda x: x[1])

    cdq(0, n - 1)

    ans = [0] * n
    for i in range(n):
        ans[f[i]] += 1
    for i in range(n):
        print(ans[i])


if __name__ == "__main__":
    solve()
