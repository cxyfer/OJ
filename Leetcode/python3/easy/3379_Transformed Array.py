#
# @lc app=leetcode id=3379 lang=python3
# @lcpr version=30204
#
# [3379] Transformed Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    三種Case，但其實可以合併成一種
    1. x > 0
    2. x < 0
    3. x == 0
"""
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        return [nums[(i + x) % len(nums)] for i, x in enumerate(nums)]
        # n = len(nums)
        # ans = [0] * n
        # for i, x in enumerate(nums):
        #     ans[i] = nums[(i + x) % n]
        # return ans
# @lc code=end



#
# @lcpr case=start
# [3,-2,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [-1,4,-1]\n
# @lcpr case=end

#

