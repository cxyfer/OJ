#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(x, y):
            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[nx][ny] == '0':
                    continue
                grid[nx][ny] = '0'
                dfs(nx, ny)

        ans = 0
        for i, row in enumerate(grid):
            for j in range(n):
                if row[j] == '0': continue
                row[j] = '0'
                dfs(i, j)
                ans += 1
        return ans
    
class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        ans = sum(1 for row in grid for ch in row if ch == '1')
        pa = [i * n + j if ch == '1' else -1 for i, row in enumerate(grid) for j, ch in enumerate(row)]
        sz = [1] * m * n

        def find(x):
            while pa[x] != x:
                pa[x] = pa[pa[x]]
                x = pa[x]
            return x
        
        def union(x, y):
            fx, fy = find(x), find(y)
            if fx == fy: return
            if sz[fx] < sz[fy]:
                fx, fy = fy, fx
            pa[fy] = fx
            sz[fx] += sz[fy]
            nonlocal ans
            ans -= 1
        
        for i, row in enumerate(grid):
            for j, ch in enumerate(row):
                if ch == '0': continue
                for nx, ny in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[nx][ny] == '0':
                        continue
                    union(i * n + j, nx * n + ny)
        return ans

Solution = Solution1
# Solution = Solution2
# @lc code=end

