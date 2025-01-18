# @algorithm @lc id=3045 lang=python3 
# @title minimum-right-shifts-to-sort-the-array

from en.Python3.mod.preImport import *
# @test([3,4,5,1,2])=2
# @test([1,3,5])=0
# @test([2,1,4])=-1
class Solution:
    """
        1. find the index of the smallest element
        2. check if the array is sorted
    """
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        # find index of smallest element
        idx = 0
        for i in range(n):
            if nums[i] < nums[idx]:
                idx = i
        # check if the array is sorted
        for i in range(n-1):
            if nums[(idx + i) % n] > nums[(idx + i + 1) % n]:
                return -1
        return (n - idx) % n