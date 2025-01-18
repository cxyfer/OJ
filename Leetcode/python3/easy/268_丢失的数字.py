#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#
from preImport import *
# @lc code=start
class Solution:
    """
        1. Math
        2. Sort
        3. Hash Table
        4. Bit Manipulation
    """
    def missingNumber(self, nums: List[int]) -> int:
        # return self.solve1(nums)
        # return self.solve2(nums)
        # return self.solve3(nums)
        return self.solve4(nums)
    def solve1(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
    def solve2(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] != 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                return nums[i] - 1
        return nums[-1] + 1
    def solve3(self, nums: List[int]) -> int:
        s = set(nums)
        for x in range(len(nums) + 1):
            if x not in s:
                return x
    def solve4(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res
# @lc code=end

