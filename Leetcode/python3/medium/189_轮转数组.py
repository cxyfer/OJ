#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#
from preImport import *
# @lc code=start
class Solution:
    """
        1. reverse all
        2. reverse first k elements
        3. reverse last n-k elements
    """
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n # k 可能大於 n
        if k == 0:
            return
        
        nums.reverse() # 1. reverse all
        nums[:k] = reversed(nums[:k]) # 2. reverse first k elements
        nums[k:] = reversed(nums[k:]) # 3. reverse last n-k elements
        
# @lc code=end

