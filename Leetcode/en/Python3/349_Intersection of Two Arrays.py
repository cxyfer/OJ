# @algorithm @lc id=349 lang=python3 
# @title intersection-of-two-arrays


from en.Python3.mod.preImport import *
# @test([1,2,2,1],[2,2])=[2]
# @test([4,9,5],[9,4,9,8,4])=[9,4]
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))