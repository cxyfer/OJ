# @algorithm @lc id=137 lang=python3 
# @title single-number-ii


from en.Python3.mod.preImport import *
# @test([2,2,3,2])=3
# @test([0,1,0,1,0,1,99])=99
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        b1, b0 = 0, 0
        for num in nums:
            b0 = b0 ^ num & ~b1
            b1 = b1 ^ num & ~b0
        return b0