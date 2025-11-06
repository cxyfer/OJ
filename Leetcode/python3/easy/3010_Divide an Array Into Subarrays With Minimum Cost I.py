#
# @lc app=leetcode id=3010 lang=python3
#
# [3010] Divide an Array Into Subarrays With Minimum Cost I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        return nums[0] + sum(nsmallest(2, nums[1:]))
# @lc code=end

