#
# @lc app=leetcode id=3701 lang=python3
#
# [3701] Compute Alternating Sum
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        return sum(nums[::2]) - sum(nums[1::2])
# @lc code=end

