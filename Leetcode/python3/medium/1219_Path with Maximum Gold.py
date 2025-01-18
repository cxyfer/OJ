#
# @lc app=leetcode id=1219 lang=python3
# @lcpr version=30201
#
# [1219] Path with Maximum Gold
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Backtracking
    """
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(x, y):
            res = 0
            origin = grid[x][y] # backup
            grid[x][y] = 0 # mark as visited
            for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != 0:
                    res = max(res, dfs(nx, ny))
            grid[x][y] = origin # backtracking
            return res + origin
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    ans = max(ans, dfs(i, j))
        return ans
# @lc code=end



#
# @lcpr case=start
# [[0,6,0],[5,8,7],[0,9,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]\n
# @lcpr case=end

#

