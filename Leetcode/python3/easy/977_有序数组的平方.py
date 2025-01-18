#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#
from preImport import *
# @lc code=start
class Solution:
    """
        Two pointers
    """
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        left, right = 0, n - 1
        # idx = n - 1
        while (left <= right):
            if abs(nums[left]) < abs(nums[right]):
                ans[right - left] = nums[right] ** 2
                right -= 1
            else:
                ans[right - left] = nums[left] ** 2
                left += 1
            # idx -= 1
        return ans
# @lc code=end

