#
# @lc app=leetcode id=2290 lang=python3
# @lcpr version=30204
#
# [2290] Minimum Obstacle Removal to Reach Corner
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[float("inf")] * n for _ in range(m)]
        dist[0][0] = 0
        hp = [(0, 0, 0)]  # (dist, x, y)
        while hp:
            d, x, y = heappop(hp)
            if d > dist[x][y]:
                continue
            if x == m - 1 and y == n - 1:
                return d
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    nd = d + grid[nx][ny]
                    if nd < dist[nx][ny]:
                        dist[nx][ny] = nd
                        heappush(hp, (nd, nx, ny))
        return -1
        
# @lc code=end



#
# @lcpr case=start
# [[0,1,1],[1,1,0],[1,1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]\n
# @lcpr case=end

#

