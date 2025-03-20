#
# @lc app=leetcode id=2376 lang=python3
#
# [2376] Count Special Integers
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countSpecialNumbers(self, high: int) -> int:
        low = list(map(int, str(1)))
        high = list(map(int, str(high)))
        n = len(high)
        diff = n - len(low)
        low = [0] * (n - len(low)) + low  # 補前導零，使 low 和 high 對齊

        @cache
        def dfs(i: int, used: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return 1

            # 第 i 個數位可以從 lo 枚舉到 hi
            # 如果對數位還有其它約束，應該只在下面的 for 迴圈做限制，不應修改 lo 或 hi
            lo = low[i] if limit_low else 0
            hi = high[i] if limit_high else 9

            res = 0             
            if i < diff and limit_low:
                res += dfs(i + 1, 0, True, False)  # 前導 0
            for d in range(1 if i < diff and limit_low else lo, hi + 1):
                if used & (1 << d):
                    continue
                res += dfs(i + 1, used | (1 << d), limit_low and d == lo, limit_high and d == hi)
            return res

        return dfs(0, 0, True, True)
# @lc code=end

sol = Solution()
print(sol.countSpecialNumbers(20))  # 19
print(sol.countSpecialNumbers(5))  # 5
print(sol.countSpecialNumbers(135))  # 110