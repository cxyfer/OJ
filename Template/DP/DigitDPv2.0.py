from functools import cache

"""
Digit DP Template v2.0
- 3490. Count Beautiful Numbers
- 2999. Count the Number of Powerful Integers
"""

class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        high = list(map(int, str(r)))
        n = len(high)
        low = list(map(int, str(l).zfill(n)))  # 補前導零，使 low 和 high 對齊
        diff = n - len(low)

        @cache
        def dfs(i: int, s: int, m: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return 1 if s and m % s == 0 else 0

            # 第 i 個數位可以從 lo 枚舉到 hi
            # 如果對數位還有其它約束，應該只在下面的 for 迴圈做限制，不應修改 lo 或 hi
            lo = low[i] if limit_low else 0
            hi = high[i] if limit_high else 9

            res = 0
            if i < diff and limit_low:
                res += dfs(i + 1, 0, 1, True, False)  # 前導 0
                # assert lo == 0
            for d in range(1 if i < diff and limit_low else lo, hi + 1):
                res += dfs(i + 1, s + d, m * d, limit_low and d ==
                           lo, limit_high and d == hi)
            return res

        return dfs(0, 0, 1, True, True)
