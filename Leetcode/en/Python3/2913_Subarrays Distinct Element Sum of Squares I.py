# @algorithm @lc id=3163 lang=python3 
# @title subarrays-distinct-element-sum-of-squares-i


from en.Python3.mod.preImport import *
# @test([1,2,1])=15
# @test([1,1])=3
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for l in range(1, n+1):
            for i in range(n-l+1):
                ans += len(set(nums[i:i+l]))** 2
        return ans