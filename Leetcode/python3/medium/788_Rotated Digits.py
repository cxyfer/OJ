#
# @lc app=leetcode id=788 lang=python3
#
# [788] Rotated Digits
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
DIFF = set([2, 5, 6, 9])  # 旋轉後不同的數字
SAME = set([0, 1, 8])  # 旋轉後相同的數字

class Solution:
    def rotatedDigits(self, n: int) -> int:
        l, r = 1, n
        diff = len(str(r)) - len(str(l))
        high = list(map(int, str(r)))
        n = len(high)
        low = list(map(int, str(l).zfill(n)))  # 補前導零，使 low 和 high 對齊

        @cache
        def dfs(i: int, has_diff: bool, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return 1 if has_diff else 0

            # 第 i 個數位可以從 lo 枚舉到 hi
            # 如果對數位還有其它約束，應該只在下面的 for 迴圈做限制，不應修改 lo 或 hi
            lo = low[i] if limit_low else 0
            hi = high[i] if limit_high else 9

            res = 0
            if i < diff and limit_low:
                res += dfs(i + 1, False, True, False)  # 前導 0
            for d in range(1 if i < diff and limit_low else lo, hi + 1):
                if d not in DIFF and d not in SAME:
                    continue
                res += dfs(
                    i + 1,
                    has_diff or d in DIFF,
                    limit_low and d == lo,
                    limit_high and d == hi,
                )
            return res

        return dfs(0, False, True, True)
# @lc code=end

sol = Solution()
print(sol.rotatedDigits(10))  # 4
print(sol.rotatedDigits(2))  # 1

