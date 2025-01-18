# @algorithm @lc id=463 lang=python3 
# @title island-perimeter


from en.Python3.mod.preImport import *
# @test([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])=16
# @test([[1]])=4
# @test([[1,0]])=4
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        land, border = 0, 0 # 土地個數、接壤邊界的條數
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    land += 1
                    if i < m-1 and grid[i+1][j] == 1:
                        border += 1
                    if j < n-1 and grid[i][j+1] == 1:
                        border += 1
        return 4*land - 2*border