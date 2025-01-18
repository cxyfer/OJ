# @algorithm @lc id=2914 lang=python3 
# @title find-the-safest-path-in-a-grid


from en.Python3.mod.preImport import *
# @test([[1,0,0],[0,0,0],[0,0,1]])=0
# @test([[0,0,1],[0,0,0],[0,0,0]])=2
# @test([[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]])=2
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        