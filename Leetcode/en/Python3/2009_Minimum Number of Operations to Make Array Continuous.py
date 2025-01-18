# @algorithm @lc id=2119 lang=python3 
# @title minimum-number-of-operations-to-make-array-continuous


from en.Python3.mod.preImport import *
# @test([4,2,5,3])=0
# @test([1,2,3,5,6])=1
# @test([1,10,100,1000])=3
class Solution:
    """
        Sliding window
    """
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums)) # remove duplicates, and sort
        m, left = len(nums), 0
        for i in range(m):
            if nums[i] - nums[left] >= n: # 確保窗口內的數字都在 [nums[left], nums[left]+n) 之間
                left += 1
        return n - (m - left) # n - m + left