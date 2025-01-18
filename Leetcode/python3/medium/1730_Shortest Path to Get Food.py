#
# @lc app=leetcode id=1730 lang=python3
# @lcpr version=30204
#
# [1730] Shortest Path to Get Food
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        st = (-1, -1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "*":
                    st = (i, j)
                    break
        # BFS
        q = deque([st])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[st[0]][st[1]] = 0
        while q:
            x, y = q.popleft()
            if grid[x][y] == "#":
                return dist[x][y]
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != "X" and dist[nx][ny] == float('inf'):
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
        return -1
    
class Solution2:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        st = (-1, -1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "*":
                    st = (i, j)
                    break
        # Level Order Traversal
        q = deque([st])
        step = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != "X":
                        if grid[nx][ny] == "#":
                            return step + 1
                        q.append((nx, ny))
                        grid[nx][ny] = "X"
            step += 1
        return -1
    
class Solution(Solution2):
    pass
# @lc code=end



#
# @lcpr case=start
# [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]\n
# @lcpr case=end

# @lcpr case=start
# [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]\n
# @lcpr case=end

# @lcpr case=start
# [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]\n
# @lcpr case=end

#

