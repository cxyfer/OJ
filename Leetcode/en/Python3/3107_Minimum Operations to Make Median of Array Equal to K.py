# @algorithm @lc id=3387 lang=python3 
# @title minimum-operations-to-make-median-of-array-equal-to-k


from en.Python3.mod.preImport import *
# @test([2,5,6,8,5],4)=2
# @test([2,5,6,8,5],7)=3
# @test([1,2,3,4,5,6],4)=0
class Solution:
    """
        Sort
        看範例即可
    """
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        m = n // 2
        ans = 0
        if nums[m] < k: # 讓中位數以右的數字增加至 k
            for i in range(m, n):
                if nums[i] >= k:
                    break
                ans += k - nums[i]
        elif nums[m] > k: # 讓中位數以左的數字減少至 k
            for i in range(m, -1, -1):
                if nums[i] <= k: 
                    break
                ans += nums[i] - k
        return ans