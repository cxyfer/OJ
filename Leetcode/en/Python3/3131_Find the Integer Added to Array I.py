# @algorithm @lc id=3397 lang=python3 
# @title find-the-integer-added-to-array-i


from en.Python3.mod.preImport import *
# @test([2,6,4],[9,7,5])=3
# @test([10],[5])=-5
# @test([1,1,1,1],[1,1,1,1])=0
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return max(nums2) - max(nums1)