# @algorithm @lc id=3178 lang=python3 
# @title minimum-increment-operations-to-make-array-beautiful


from en.Python3.mod.preImport import *
# @test([2,3,0,0,2],4)=3
# @test([0,1,3,3],5)=2
# @test([1,1,2],1)=0
class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        