# @algorithm @lc id=1331 lang=python3 
# @title path-with-maximum-gold


from en.Python3.mod.preImport import *
# @test([[0,6,0],[5,8,7],[0,9,0]])=24
# @test([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]])=28
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        