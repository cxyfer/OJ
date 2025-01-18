# @algorithm @lc id=733 lang=python3 
# @title flood-fill


from en.Python3.mod.preImport import *
# @test([[1,1,1],[1,1,0],[1,0,1]],1,1,2)=[[2,2,2],[2,2,0],[2,0,1]]
# @test([[0,0,0],[0,0,0]],0,0,0)=[[0,0,0],[0,0,0]]
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        