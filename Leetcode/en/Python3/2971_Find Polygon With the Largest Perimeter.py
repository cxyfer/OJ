# @algorithm @lc id=3262 lang=python3 
# @title find-polygon-with-the-largest-perimeter


from en.Python3.mod.preImport import *
# @test([5,5,5])=15
# @test([1,12,1,2,5,50,3])=12
# @test([5,5,50])=-1
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        # pre = list(accumulate(nums, initial=0))
        s = sum(nums)
        for i in range(n - 1, 1, -1):
            # if pre[i] > nums[i]:
            #     return pre[i] + nums[i]
            if s  > 2 * nums[i]: # s - nums[i] > nums[i]
                return s
            s -= nums[i]
        return -1
        