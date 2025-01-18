# @algorithm @lc id=3402 lang=python3 
# @title minimum-cost-to-equalize-array


from en.Python3.mod.preImport import *
# @test([4,1],5,2)=15
# @test([2,3,3,3,5],2,1)=6
# @test([3,5,3],1,3)=4
class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        