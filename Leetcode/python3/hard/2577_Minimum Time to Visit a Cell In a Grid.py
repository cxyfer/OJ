#
# @lc app=leetcode id=2577 lang=python3
# @lcpr version=30204
#
# [2577] Minimum Time to Visit a Cell In a Grid
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        if grid[0][1] > 1 and grid[1][0] > 1:  # 无法「等待」
            return -1
        
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        hp = [(0, 0, 0)]
        while hp:
            d, x, y = heappop(hp)
            if d > dist[x][y]: continue
            if x == m - 1 and y == n - 1:
                return d
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    nd = max(d + 1, grid[nx][ny])
                    nd += (nd - nx - ny) % 2
                    if nd < dist[nx][ny]:
                        dist[nx][ny] = nd
                        heappush(hp, (nd, nx, ny))
        return -1
# @lc code=end



#
# @lcpr case=start
# [[0,1,3,2],[5,1,2,5],[4,3,8,6]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,2,4],[3,2,1],[1,0,4]]\n
# @lcpr case=end

#

