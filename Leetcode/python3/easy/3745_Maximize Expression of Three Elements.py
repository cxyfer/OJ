#
# @lc app=leetcode id=3745 lang=python3
#
# [3745] Maximize Expression of Three Elements
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        # return sum(nlargest(2, nums)) - min(nums)
        nums.sort()
        return nums[-1] + nums[-2] - nums[0]
# @lc code=end

