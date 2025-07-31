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
        # return max(nums) if not (pos := set(x for x in nums if x > 0)) else sum(pos)
        pos = set()
        for x in nums:
            if x > 0 and x not in pos:
                pos.add(x)
        return sum(pos) if pos else max(nums)
# @lc code=end

