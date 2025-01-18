#
# @lc app=leetcode id=3286 lang=python3
# @lcpr version=30204
#
# [3286] Find a Safe Walk Through a Grid
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        n, m = len(grid), len(grid[0])

        # BFS 找最短路徑
        q = deque([(0, 0, grid[0][0])])
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = grid[0][0]
        while q:
            x, y, h = q.popleft()
            if x == n - 1 and y == m - 1:
                if h < health:
                    return True
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if h + grid[nx][ny] < dist[nx][ny]:
                        dist[nx][ny] = h + grid[nx][ny]
                        q.append((nx, ny, h + grid[nx][ny]))
        return False
# @lc code=end



#
# @lcpr case=start
# [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]\n1\n
# @lcpr case=end

# @lcpr case=start
# [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]]\n3\n
# @lcpr case=end

# @lcpr case=start
# [[1,1,1],[1,0,1],[1,1,1]]\n5\n
# @lcpr case=end

#

