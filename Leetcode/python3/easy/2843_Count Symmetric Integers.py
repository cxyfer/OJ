#
# @lc app=leetcode id=2843 lang=python3
#
# [2843]   Count Symmetric Integers
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. Brute Force
2. Digit DP
  - sum(former) == sum(latter) -> sum(former) - sum(latter) == 0
  - j: 前半部分已經選了幾個數字
  - s: 前半部分數字和 - 後半部分數字和
"""
# @lc code=start
class Solution1:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for x in range(low, high + 1):
            lst = list(map(int, str(x)))
            if len(lst) & 1:
                continue
            ans += sum(lst[:len(lst)//2]) == sum(lst[len(lst)//2:])
        return ans

class Solution2:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        low = list(map(int, str(low)))
        high = list(map(int, str(high)))
        n = len(high)
        diff = n - len(low)
        low = [0] * (n - len(low)) + low  # 補前導零，使 low 和 high 對齊

        @cache
        def dfs(i: int, j: int, s: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return (j > 0 and s == 0)
            
            if s < 0:  # Pruning
                return 0

            # 第 i 個數位可以從 lo 枚舉到 hi
            # 如果對數位還有其它約束，應該只在下面的 for 迴圈做限制，不應修改 lo 或 hi
            lo = low[i] if limit_low else 0
            hi = high[i] if limit_high else 9

            is_former = j < n - i
            if is_former and j and (j + n - i) & 1:  # 長度必須是偶數
                return 0
            
            res = 0
            for d in range(lo, hi + 1):
                res += dfs(i + 1,
                           j + (is_former and (j > 0 or d > 0)),
                           s + (d if is_former else -d),
                           limit_low and d == lo,
                           limit_high and d == hi)
            return res

        return dfs(0, 0, 0, True, True)

# Solution = Solution1
Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.countSymmetricIntegers(1, 100))  # 9
print(sol.countSymmetricIntegers(1200, 1230))  # 4
print(sol.countSymmetricIntegers(100, 1782))  # 44
