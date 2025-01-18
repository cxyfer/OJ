# @algorithm @lc id=1988 lang=python3 
# @title minimize-maximum-pair-sum-in-array


from en.Python3.mod.preImport import *
# @test([3,5,2,3])=7
# @test([3,5,4,2,4,6])=8
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n // 2):
            ans = max(ans, nums[i] + nums[n - 1 - i])
        return ans