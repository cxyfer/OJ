#
# @lc app=leetcode.cn id=2824 lang=python3
#
# [2824] 统计和小于目标的下标对数目
#
from preImport import *
# @lc code=start
class Solution:
    """
        1. Brute Force
        2. Sort + Two Pointers
        > 基础算法精讲 01
    """
    def countPairs(self, nums: List[int], target: int) -> int:
        # return self.solve1(nums, target)
        return self.solve2(nums, target)
    """
        1. Brute Force
        Time: O(n^2)
    """ 
    def solve1(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] < target:
                    ans += 1
        return ans 
    """
        2. Sort + Two Pointers
        Time: O(nlogn)
    """
    def solve2(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        nums.sort()
        left, right = 0, n-1
        while left < right: # 區間內至少有兩個數字
            if nums[left] + nums[right] < target: 
                ans += right - left # 固定左邊的數字，右邊的數字可以是 nums[left+1] ~ nums[right]，共 right - left 個
                left += 1
            else:
                right -= 1
        return ans
# @lc code=end

