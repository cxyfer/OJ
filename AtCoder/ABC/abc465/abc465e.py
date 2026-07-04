MOD = 998244353


def solve():
    r = input().strip()
    l = 1

    n = len(r)
    diff = n - len(str(l))
    high = list(map(int, str(r)))
    low = list(map(int, str(l).zfill(n)))  # 補前導零，使 low 和 high 對齊

    memo = [[[-1] * (1 << 10) for _ in range(3)] for _ in range(n)]

    # @cache
    def dfs(i: int, s: int, msk: int, limit_low: bool, limit_high: bool) -> int:
        if i == n:
            return ((s == 0) + (msk.bit_count() == 3) + ((msk >> 3) & 1)) == 1

        if not limit_low and not limit_high and memo[i][s][msk] != -1:
            return memo[i][s][msk]

        # 第 i 個數位可以從 lo 枚舉到 hi
        # 如果對數位還有其它約束，應該只在下面的 for 迴圈做限制，不應修改 lo 或 hi
        st = lo = low[i] if limit_low else 0
        hi = high[i] if limit_high else 9

        res = 0
        if i < diff and limit_low:
            res += dfs(i + 1, 0, 0, True, False)  # 前導 0
            st = 1
        for d in range(st, hi + 1):
            res += dfs(i + 1, (s + d) % 3, msk | (1 << d), limit_low and d == lo, limit_high and d == hi)
        memo[i][s][msk] = res % MOD
        return res % MOD

    ans = dfs(0, 0, 0, True, True)
    print(ans)


if __name__ == "__main__":
    solve()
