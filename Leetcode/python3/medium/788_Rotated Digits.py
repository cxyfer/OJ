#
# @lc app=leetcode id=788 lang=python3
#
# [788] Rotated Digits
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MARKS = [0, 0, 1, -1, -1, 1, 1, -1, 0, 1]  # 0: 旋轉後相同, 1: 旋轉後不同, -1: 不能旋轉
class Solution:
    def rotatedDigits(self, n: int) -> int:
        low = list(map(int, str(0)))
        high = list(map(int, str(n)))
        n = len(high)
        low = [0] * (n - len(low)) + low  # 補前導零，使 low 和 high 對齊

        @cache
        def dfs(i: int, has_diff: bool, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return has_diff

            # 第 i 個數位可以從 lo 枚舉到 hi
            # 如果對數位還有其它約束，應該只在下面的 for 迴圈做限制，不應修改 lo 或 hi
            lo = low[i] if limit_low else 0
            hi = high[i] if limit_high else 9
            
            res = 0
            for d in range(lo, hi + 1):
                if MARKS[d] == -1:
                    continue
                res += dfs(i + 1, has_diff or MARKS[d], limit_low and d == lo, limit_high and d == hi)
            return res

        return dfs(0, False, True, True)
# @lc code=end

sol = Solution()
print(sol.rotatedDigits(10))  # 4
print(sol.rotatedDigits(2))  # 1

