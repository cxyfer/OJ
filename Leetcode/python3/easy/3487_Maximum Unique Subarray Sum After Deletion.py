#
# @lc app=leetcode id=3487 lang=python3
#
# [3487] Maximum Unique Subarray Sum After Deletion
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans = 0
        vis = set()
        for x in nums:
            if x >= 0 and x not in vis:
                vis.add(x)
                ans += x
        return ans if vis else max(nums)
# @lc code=end

