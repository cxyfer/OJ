def solve1():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    ans = 0

    # Merge Sort
    tmp = [0] * n

    def dfs(l: int, r: int) -> None:
        nonlocal ans
        if l == r:
            return
        mid = (l + r) // 2
        dfs(l, mid)
        dfs(mid + 1, r)

        i, j = l, mid + 1
        k = l
        while k <= r:
            if j > r or (i <= mid and A[i] <= A[j]):
                tmp[k] = A[i]
                i += 1
            else:
                tmp[k] = A[j]
                j += 1
                ans += mid - i + 1
            k += 1

        for i in range(l, r + 1):
            A[i] = tmp[i]

    dfs(0, n - 1)
    print(ans)


class BIT:  # PURQ, 1-based
    __slots__ = ["tree"]

    def __init__(self, n: int):
        self.tree = [0] * (n + 1)

    def add(self, k: int, x: int) -> None:  # 令 nums[k] += x
        while k < len(self.tree):
            self.tree[k] += x
            k += k & -k

    def preSum(self, k: int) -> int:  # 求 nums[1...k] 之和
        res = 0
        while k > 0:
            res += self.tree[k]
            k -= k & -k
        return res

    def query(self, l: int, r: int) -> int:  # 求 nums[l...r] 之和
        if l > r:
            return 0
        return self.preSum(r) - self.preSum(l - 1)


def solve2():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    # 離散化
    mp = {x: i for i, x in enumerate(sorted(set(A)), start=1)}
    m = len(mp)

    bit = BIT(m)
    ans = 0
    for x in A:
        ans += bit.query(mp[x] + 1, m)
        bit.add(mp[x], 1)
    print(ans)


# solve = solve1
solve = solve2

if __name__ == "__main__":
    solve()
