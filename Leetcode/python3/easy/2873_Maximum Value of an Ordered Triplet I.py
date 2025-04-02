#
# @lc app=leetcode id=2873 lang=python3
#
# [2873] Maximum Value of an Ordered Triplet I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        suf = [0] * n
        suf[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suf[i] = max(suf[i + 1], nums[i])
        ans = 0
        pre_mx = nums[0]
        for i in range(1, n - 1):
            ans = max(ans, (pre_mx - nums[i]) * suf[i + 1])
            pre_mx = max(pre_mx, nums[i])
        return ans
# @lc code=end

