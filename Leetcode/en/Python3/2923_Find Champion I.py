# @algorithm @lc id=3188 lang=python3 
# @title find-champion-i


from en.Python3.mod.preImport import *
# @test([[0,1],[0,0]])=0
# @test([[0,0,1],[1,0,1],[0,0,0]])=1
class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for j in range(n):
            flag = True
            for i in range(n):
                if grid[i][j] == 1:
                    flag = False
                    break
            if flag:
                return j
        