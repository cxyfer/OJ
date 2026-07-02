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
"""
1. Dijkstra
2. 0/1 BFS
"""


class Solution1:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        n, m = len(grid), len(grid[0])

        # Dijkstra
        dist = [[float("inf")] * m for _ in range(n)]
        dist[0][0] = grid[0][0]
        hp = [(grid[0][0], 0, 0)]
        while hp:
            d, x, y = heappop(hp)
            if x == n - 1 and y == m - 1:
                return d < health
            for nx, ny in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
                if 0 <= nx < n and 0 <= ny < m:
                    w = grid[nx][ny]
                    if (nd := d + w) < dist[nx][ny]:
                        dist[nx][ny] = nd
                        heappush(hp, (nd, nx, ny))
        return False


class Solution2:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        n, m = len(grid), len(grid[0])

        # 0/1 BFS
        dist = [[float("inf")] * m for _ in range(n)]
        dist[0][0] = grid[0][0]
        q = deque([(0, 0, grid[0][0])])
        while q:
            x, y, d = q.popleft()
            if x == n - 1 and y == m - 1:
                return d < health
            for nx, ny in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
                if 0 <= nx < n and 0 <= ny < m:
                    w = grid[nx][ny]
                    if (nd := d + w) < dist[nx][ny]:
                        dist[nx][ny] = nd
                        if w == 0:
                            q.appendleft((nx, ny, nd))
                        else:
                            q.append((nx, ny, nd))
        return False


# Solution = Solution1
Solution = Solution2
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

