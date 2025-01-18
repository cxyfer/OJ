#
# @lc app=leetcode.cn id=8039 lang=python3
#
# [8039] 使数组成为递增数组的最少右移次数
#
from en.Python3.mod.preImport import *
"""
    2855. Minimum Right Shifts to Sort the Array
"""
# @lc code=start
class Solution:
    """
        1. find the index of the smallest element
        2. check if the array is sorted
    """
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        # find index of smallest element
        idx = 0
        for i in range(n):
            if nums[i] < nums[idx]:
                idx = i
        # check if the array is sorted
        for i in range(n-1):
            if nums[(idx + i) % n] > nums[(idx + i + 1) % n]:
                return -1
        return (n - idx) % n
# @lc code=end

