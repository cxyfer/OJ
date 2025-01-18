# @algorithm @lc id=334 lang=python3 
# @title increasing-triplet-subsequence


from en.Python3.mod.preImport import *
# @test([1,2,3,4,5])=true
# @test([5,4,3,2,1])=false
# @test([2,1,5,0,4,6])=true
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        first, second = nums[0], float('inf')
        for i in range(1, n):
            if nums[i] > second:
                return True
            elif nums[i] > first:
                second = nums[i]
            else:
                first = nums[i]
        return False