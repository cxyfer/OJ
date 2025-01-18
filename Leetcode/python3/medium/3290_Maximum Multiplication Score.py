#
# @lc app=leetcode id=3290 lang=python3
# @lcpr version=30204
#
# [3290] Maximum Multiplication Score
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:

        # 考慮到前 i 個數字，選擇了 j 個數字
        @cache
        def dfs(i: int, j: int) -> int:
            if i == len(b):
                if j < len(a):
                    return float('-inf')
                return 0
            if j == len(a):
                return 0
            res = -float('inf')
            res = max(res, dfs(i + 1, j + 1) + a[j] * b[i]) # 選擇 a[j] * b[i]
            res = max(res, dfs(i + 1, j)) # 不選擇 a[j] * b[i]
            return res
        
        return dfs(0, 0)
# @lc code=end

sol = Solution()
print(sol.maxScore([3,2,5,6], [2,-6,4,-5,-3,2,-7])) # 26
print(sol.maxScore([-1,4,5,-2], [-5,-1,-3,-2,-4])) # -1

#
# @lcpr case=start
# [3,2,5,6]\n[2,-6,4,-5,-3,2,-7]\n
# @lcpr case=end

# @lcpr case=start
# [-1,4,5,-2]\n[-5,-1,-3,-2,-4]\n
# @lcpr case=end

#

