#
# @lc app=leetcode id=1391 lang=python3
#
# [1391] Check if There is a Valid Path in a Grid
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
# 右左下上分別對應 0, 1, 2, 3，這樣 d ^ 1 就是對應的反方向
DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]  
# 如果要往右走，需要當前格子有右出口，且下一個格子有左出口，其他方向同理
# 維護有四種方向出口的格子種類
MAPS = [{1, 4, 6}, {1, 3, 5}, {2, 3, 4}, {2, 5, 6}]

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        vis = [[False] * m for _ in range(n)]
        def dfs(i: int, j: int) -> bool:
            if i == n - 1 and j == m - 1:
                return True
            vis[i][j] = True
            cur = grid[i][j]
            for d, (dx, dy) in enumerate(DIRS):
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < m and not vis[nx][ny]:
                    if cur in MAPS[d] and grid[nx][ny] in MAPS[d ^ 1]:
                        if dfs(nx, ny):
                            return True
            return False
        return dfs(0, 0)
# @lc code=end

