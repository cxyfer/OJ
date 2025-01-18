# @algorithm @lc id=2606 lang=python3 
# @title difference-between-ones-and-zeros-in-row-and-column


from en.Python3.mod.preImport import *
# @test([[0,1,1],[1,0,1],[0,0,1]])=[[0,0,4],[0,0,4],[-2,-2,2]]
# @test([[1,1,1],[1,1,1]])=[[5,5,5],[5,5,5]]
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        rows = [0] * m
        cols = [0] * n
        for i in range(m):
            for j in range(n):
                rows[i] += grid[i][j]
                cols[j] += grid[i][j]
        diff = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # diff[i][j] = rows[i] + cols[j] - (n - rows[i]) - (m - cols[j])
                diff[i][j] = 2 * rows[i] + 2 * cols[j] - m - n
        return diff