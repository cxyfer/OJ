# @algorithm @lc id=162 lang=python3 
# @title find-peak-element


from en.Python3.mod.preImport import *
# @test([1,2,3,1])=2
# @test([1,2,1,3,5,6,4])=5
class Solution:
    """
        1. Simple Linear Search
    """
    # def findPeakElement(self, nums: List[int]) -> int:
    #     ans = 0
    #     for i in range(1, len(nums)):
    #         if nums[i] > nums[ans]:
    #             ans = i
    #     return ans
    """
        2. Binary Search
    """
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n-1
        while(left < right):
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left