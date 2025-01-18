# @algorithm @lc id=200 lang=python3 
# @title number-of-islands


from en.Python3.mod.preImport import *
# @test([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])=1
# @test([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])=3
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        def dfs(i,j):
            if 0<=i<m and 0<=j<n and grid[i][j]=='1':
                grid[i][j] = '0'
                for nx, ny in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
                    dfs(nx, ny)
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    ans += 1
                    dfs(i,j)
        return ans