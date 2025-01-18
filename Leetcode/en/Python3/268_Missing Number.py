# @algorithm @lc id=268 lang=python3 
# @title missing-number


from en.Python3.mod.preImport import *
# @test([3,0,1])=2
# @test([0,1])=2
# @test([9,6,4,2,3,5,7,0,1])=8
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