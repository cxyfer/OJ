#
# @lc app=leetcode id=1368 lang=python3
# @lcpr version=30204
#
# [1368] Minimum Cost to Make at Least One Valid Path in a Grid
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0
        hp = [(0, 0, 0)]
        while hp:
            d, x, y = heappop(hp)
            if x == n - 1 and y == m - 1:
                return d
            for i, (dx, dy) in enumerate(D, start=1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    nd = d if grid[x][y] == i else (d + 1)
                    if nd < dist[nx][ny]:
                        dist[nx][ny] = nd
                        heappush(hp, (nd, nx, ny))
        return -1  # 其實不可能無解
# @lc code=end



#
# @lcpr case=start
# [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1,3],[3,2,2],[1,1,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[4,3]]\n
# @lcpr case=end

#

