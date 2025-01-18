# @algorithm @lc id=941 lang=python3 
# @title sort-array-by-parity


from en.Python3.mod.preImport import *
# @test([3,1,2,4])=[2,4,3,1]
# @test([0])=[0]
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x: x % 2)
        