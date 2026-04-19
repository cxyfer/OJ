#
# @lc app=leetcode id=1855 lang=python3
#
# [1855] Maximum Distance Between a Pair of Values
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        ans = i = 0
        for j, y in enumerate(nums2):
            while i < n and nums1[i] > y:
                i += 1
            if i == n:
                break
            ans = max(ans, j - i)
        return ans
# @lc code=end

