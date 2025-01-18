#
# @lc app=leetcode id=3342 lang=python3
# @lcpr version=30204
#
# [3342] Find Minimum Time to Reach Last Room II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        DIR = [(-1,0), (1,0), (0,-1), (0,1)]
        
        # dist = [[[float('inf')] * 2 for _ in range(m)] for _ in range(n)]
        # dist[0][0][0] = 0
        # hp = [(0, 0, 0, 0)] # (time, x, y, z)
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0
        hp = [(0, 0, 0)] # (time, x, y)      
        while hp:
            # t, x, y, z = heappop(hp)
            t, x, y = heappop(hp)
            if x == n - 1 and y == m - 1:
                return t
            # if t > dist[x][y][z]: continue
            if t > dist[x][y]: continue
            for dx, dy in DIR:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    # nt = max(t, moveTime[nx][ny]) + (1 if z == 0 else 2)
                    # nz = 1 - z
                    # if nt < dist[nx][ny][nz]:
                    #     dist[nx][ny][nz] = nt
                    #     heappush(hp, (nt, nx, ny, nz))
                    nt = max(t, moveTime[nx][ny]) + (2 if (x + y) & 1 else 1)
                    if nt < dist[nx][ny]:
                        dist[nx][ny] = nt
                        heappush(hp, (nt, nx, ny))
        return -1
# @lc code=end

sol = Solution()
print(sol.minTimeToReach([[0,4],[4,4]])) # 7
print(sol.minTimeToReach([[0,0,0,0],[0,0,0,0]])) # 6
print(sol.minTimeToReach([[0,1],[1,2]])) # 4

#
# @lcpr case=start
# [[0,4],[4,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0,0,0],[0,0,0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1],[1,2]]\n
# @lcpr case=end

#

