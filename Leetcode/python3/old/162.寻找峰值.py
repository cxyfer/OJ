#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    """
        1. Simple Linear Search
    """
    # def findPeakElement(self, nums: List[int]) -> int:
    #     ans = 0
    #     for i in range(1, len(nums)):
    #         if nums[i] > nums[ans]:
    #             ans = i
    #     return ans
    """
        2. Binary Search
    """
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n-1
        while(left < right):
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left
# @lc code=end

