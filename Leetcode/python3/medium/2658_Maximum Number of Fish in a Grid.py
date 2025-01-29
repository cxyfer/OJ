#
# @lc app=leetcode id=2658 lang=python3
# @lcpr version=30204
#
# [2658] Maximum Number of Fish in a Grid
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        def dfs(x, y):
            res = grid[x][y]
            grid[x][y] = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny]:
                    res += dfs(nx, ny)
            return res

        ans = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 0:
                    continue
                # ans = max(ans, dfs(i, j))
                st = [(i, j)]
                res = 0
                while st:
                    x, y = st.pop()
                    res += grid[x][y]
                    grid[x][y] = 0
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny]:
                            st.append((nx, ny))
                ans = max(ans, res)
        return ans
# @lc code=end



#
# @lcpr case=start
# [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]\n
# @lcpr case=end

#

