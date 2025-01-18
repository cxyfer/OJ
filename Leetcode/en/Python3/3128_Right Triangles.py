# @algorithm @lc id=3388 lang=python3 
# @title right-triangles


from en.Python3.mod.preImport import *
# @test([[0,1,0],[0,1,1],[0,1,0]])=2
# @test([[1,0,0,0],[0,1,0,1],[1,0,0,0]])=0
# @test([[1,0,1],[1,0,0],[1,0,0]])=2
class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        