# @algorithm @lc id=324 lang=python3 
# @title wiggle-sort-ii


from en.Python3.mod.preImport import *
# @test([1,5,1,1,6,4])=[1,6,1,5,1,4]
# @test([1,3,2,2,3,1])=[2,3,1,3,1,2]
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        