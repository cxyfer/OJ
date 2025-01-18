# @algorithm @lc id=932 lang=python3 
# @title monotonic-array


from en.Python3.mod.preImport import *
# @test([1,2,2,3])=true
# @test([6,5,4,4])=true
# @test([1,3,2])=false
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        res1, res2 = True, True
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                res1 = False
            if nums[i] > nums[i-1]:
                res2 = False
        return res1 or res2