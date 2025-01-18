#
# @lc app=leetcode id=994 lang=python3
# @lcpr version=30201
#
# [994] Rotting Oranges
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        BFS
    """
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 2:
                    q.append((i, j, 0)) # (x, y, t)
        ans = 0
        while q:
            ans = q[0][2]
            for _ in range(len(q)):
                x, y, t = q.popleft()
                for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1: # 新鮮的橘子
                        grid[nx][ny] = 2 # 腐爛了
                        q.append((nx, ny, t+1))
        for i, row in enumerate(grid): # 檢查還有沒有新鮮的橘子
            for j, x in enumerate(row):
                if x == 1:
                    return -1
        return ans 
# @lc code=end



#
# @lcpr case=start
# [[2,1,1],[1,1,0],[0,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[2,1,1],[0,1,1],[1,0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,2]]\n
# @lcpr case=end

#

