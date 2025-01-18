# @algorithm @lc id=3151 lang=python3 
# @title minimum-processing-time


from en.Python3.mod.preImport import *
# @test([8,10],[2,2,3,1,8,7,4,5])=16
# @test([10,20],[2,3,1,2,5,8,4,3])=23
class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        