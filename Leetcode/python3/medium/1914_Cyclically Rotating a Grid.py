#
# @lc app=leetcode id=1914 lang=python3
#
# [1914] Cyclically Rotating a Grid
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers = min(m // 2, n // 2)
        for layer in range(layers):
            pos = []
            val = []
            x1, x2 = layer, m - layer - 1
            y1, y2 = layer, n - layer - 1
            for i in range(x1, x2):  # left
                pos.append((i, y1))
                val.append(grid[i][y1])
            for j in range(y1, y2):  # down
                pos.append((x2, j))
                val.append(grid[x2][j])
            for i in range(x2, x1, -1):  # right
                pos.append((i, y2))
                val.append(grid[i][y2])
            for j in range(y2, y1, -1):  # up
                pos.append((layer, j))
                val.append(grid[layer][j])

            sz = len(pos)
            kk = k % sz
            for i, (r, c) in enumerate(pos):
                grid[r][c] = val[(i - kk) % sz]
        return grid
# @lc code=end

sol = Solution()
print(sol.rotateGrid([[40,10],[30,20]], 1))  # [[10,20],[40,30]]
print(sol.rotateGrid([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 2))
