#
# @lc app=leetcode id=2302 lang=python3
#
# [2302] Count Subarrays With Score Less Than K
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = left = s = 0
        for right, x in enumerate(nums):
            s += x
            while s * (right - left + 1) >= k:
                s -= nums[left]
                left += 1
            ans += right - left + 1  # [left, right], [left+1, right], [left+2, right], ..., [right, right]
        return ans
# @lc code=end

