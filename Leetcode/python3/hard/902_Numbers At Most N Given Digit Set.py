#
# @lc app=leetcode id=902 lang=python3
#
# [902] Numbers At Most N Given Digit Set
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], hi: int) -> int:
        digits = list(map(int, digits))

        low = list(map(int, str(0)))
        high = list(map(int, str(hi)))
        n = len(high)
        low = [0] * (n - len(low)) + low  # 補前導零，使 low 和 high 對齊

        @cache
        def dfs(i: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return 1
            
            # 第 i 個數位可以從 lo 枚舉到 hi
            # 如果對數位還有其它約束，應該只在下面的 for 迴圈做限制，不應修改 lo 或 hi
            lo = low[i] if limit_low else 0
            hi = high[i] if limit_high else 9

            res = 0
            if limit_low:  # 前導 0
                res += dfs(i + 1, True, False)
            for d in digits:
                if d < lo or d > hi:
                    continue
                res += dfs(i + 1, limit_low and d == lo, limit_high and d == hi)
            return res

        return dfs(0, True, True) - 1

        
# @lc code=end

sol = Solution()
# print(sol.atMostNGivenDigitSet(["1", "3", "5", "7"], 100))  # 20
# print(sol.atMostNGivenDigitSet(["1", "3", "5", "7"], 10000))  # 52
print(sol.atMostNGivenDigitSet(["1", "4", "9"], 1000000000))  # 29523
# print(sol.atMostNGivenDigitSet(["7"], 8))  # 1


