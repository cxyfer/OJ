#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max(sum(g) for _, g in groupby(nums))
# @lc code=end

sol = Solution()
print(sol.findMaxConsecutiveOnes([1,1,0,1,1,1])) # 3
print(sol.findMaxConsecutiveOnes([0])) # 3