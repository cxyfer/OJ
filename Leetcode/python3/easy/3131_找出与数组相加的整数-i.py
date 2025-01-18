#
# @lc app=leetcode.cn id=3131 lang=python3
#
# [3131] 找出与数组相加的整数 I
#
from preImport import *
# @lc code=start
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return max(nums2) - max(nums1)
# @lc code=end

