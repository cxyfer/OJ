# @algorithm @lc id=1396 lang=python3 
# @title count-servers-that-communicate


from en.Python3.mod.preImport import *
from collections import Counter
# @test([[1,0],[0,1]])=0
# @test([[1,0],[1,1]])=3
# @test([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]])=4
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # Use Counter() to replace List to save memory ?
        m, n = len(grid), len(grid[0])
        # row, col = [0]*m, [0]*n
        row, col = Counter(), Counter()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row[i] > 1 or col[j] > 1):
                    ans += 1
        return ans