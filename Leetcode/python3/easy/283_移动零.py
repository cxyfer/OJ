2#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
from preImport import *
# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # slow, fast = 0, 0
        # while fast < n:
        #     if nums[fast] != 0:
        #         nums[slow] = nums[fast]
        #         slow += 1
        #     fast += 1
        # while slow < n:
        #     nums[slow] = 0
        #     slow += 1
        last = 0 # last non-zero element
        for i in range(n):
            if nums[i] != 0:
                nums[last] = nums[i]
                last += 1
        for i in range(last, n):
            nums[i] = 0

# @lc code=end

