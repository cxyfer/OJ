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
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                    grid[nx][ny] = "0"
                    dfs(nx, ny)

        ans = 0
        for i, row in enumerate(grid):
            for j, ch in enumerate(row):
                if ch == "1":
                    row[j] = "0"
                    dfs(i, j)
                    ans += 1
        return ans


class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        ans = sum(1 for row in grid for ch in row if ch == "1")
        fa = list(range(m * n))
        sz = [1] * (m * n)

        def find(x):
            while fa[x] != x:
                fa[x] = fa[fa[x]]
                x = fa[x]
            return x

        def union(x, y):
            fx, fy = find(x), find(y)
            if fx == fy:
                return
            if sz[fx] < sz[fy]:
                fx, fy = fy, fx
            fa[fy] = fx
            sz[fx] += sz[fy]
            nonlocal ans
            ans -= 1

        for i, row in enumerate(grid):
            for j, ch in enumerate(row):
                if ch == "1":
                    # 只需檢查右邊和下邊，避免重複合併
                    for nx, ny in [(i + 1, j), (i, j + 1)]:
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                            union(i * n + j, nx * n + ny)
        return ans


# Solution = Solution1
Solution = Solution2
# @lc code=end

