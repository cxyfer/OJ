# @algorithm @lc id=1018 lang=python3 
# @title largest-perimeter-triangle


from en.Python3.mod.preImport import *
# @test([2,1,2])=5
# @test([1,2,1,10])=0
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse=True)
        for i in range(n-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0