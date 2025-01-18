# @algorithm @lc id=643 lang=python3 
# @title maximum-average-subarray-i


from en.Python3.mod.preImport import *
# @test([1,12,-5,-6,50,3],4)=12.75000
# @test([5],1)=5.00000
class Solution:
    """
        Sliding window
    """
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        cur = sum(nums[:k])
        ans = cur
        for idx in range(k, n):
            cur += nums[idx] - nums[idx-k] # sliding window
            ans = max(ans, cur)
        return ans / k