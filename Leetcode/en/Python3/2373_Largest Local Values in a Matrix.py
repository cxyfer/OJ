# @algorithm @lc id=2454 lang=python3 
# @title largest-local-values-in-a-matrix


from en.Python3.mod.preImport import *
# @test([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]])=[[9,9],[8,6]]
# @test([[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]])=[[2,2,2],[2,2,2],[2,2,2]]
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for i in range(n-2):
            for j in range(n-2):
                grid[i][j] = max( max(row[j:j+3]) for row in grid[i:i+3])
            grid[i].pop()
            grid[i].pop()
        grid.pop()
        grid.pop()
        return grid