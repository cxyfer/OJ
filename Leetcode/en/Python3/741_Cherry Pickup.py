# @algorithm @lc id=741 lang=python3 
# @title cherry-pickup


from en.Python3.mod.preImport import *
# @test([[0,1,-1],[1,0,-1],[1,1,1]])=5
# @test([[1,1,-1],[1,-1,1],[-1,1,1]])=0
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        