#
# @lc app=leetcode id=1874 lang=python3
#
# [1874] Minimize Product Sum of Two Arrays
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort(reverse=True)
        return sum(a * b for a, b in zip(nums1, nums2))
# @lc code=end

