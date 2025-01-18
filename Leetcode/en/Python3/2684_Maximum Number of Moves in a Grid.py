# @algorithm @lc id=2794 lang=python3 
# @title maximum-number-of-moves-in-a-grid


from en.Python3.mod.preImport import *
# @test([[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]])=3
# @test([[3,2,4],[2,1,9],[1,1,7]])=0
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        @cache
        def dfs(i, j, v):
            res = v
            for dx, dy in [(-1, 1), (0, 1), (1, 1)]:
                x, y = i + dx, j + dy
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] > grid[i][j]:
                    res = max(res, dfs(x, y, v+1))
            return res
        return max(dfs(i, 0, 0) for i in range(m))