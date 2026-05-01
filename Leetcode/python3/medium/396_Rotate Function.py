#
# @lc app=leetcode id=396 lang=python3
#
# [396] Rotate Function
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        ans = f = sum(i * x for i, x in enumerate(nums))
        for i in range(n - 1, 0, -1):
            f += s - n * nums[i]
            ans = max(ans, f)
        return ans
# @lc code=end

