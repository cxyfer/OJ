# @algorithm @lc id=283 lang=python3 
# @title move-zeroes


from en.Python3.mod.preImport import *
# @test([0,1,0,3,12])=[1,3,12,0,0]
# @test([0])=[0]
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        slow, fast = 0, 0
        while fast < n:
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        while slow < n:
            nums[slow] = 0
            slow += 1
        