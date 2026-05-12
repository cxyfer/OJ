from functools import cache


def solve():
    l, r = map(int, input().split())

    high = list(map(int, str(r)))
    n = len(high)
    low = list(map(int, str(l).zfill(n)))  # 補前導零，使 low 和 high 對齊

    @cache
    def dfs(i: int, top: int, limit_low: bool, limit_high: bool) -> int:
        if i == n:
            return 1 if top > 0 else 0

        # 第 i 個數位可以從 lo 枚舉到 hi
        # 如果對數位還有其它約束，應該只在下面的 for 迴圈做限制，不應修改 lo 或 hi
        lo = low[i] if limit_low else 0
        hi = high[i] if limit_high else 9

        res = 0
        for d in range(lo, hi + 1):
            if top == 0:
                res += dfs(i + 1, d, limit_low and d == lo, limit_high and d == hi)
            elif d < top:
                res += dfs(i + 1, top, limit_low and d == lo, limit_high and d == hi)
        return res

    ans = dfs(0, 0, True, True)
    dfs.cache_clear()
    print(ans)


if __name__ == "__main__":
    solve()
