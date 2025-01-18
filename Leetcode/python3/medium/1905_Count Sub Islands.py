#
# @lc app=leetcode id=1905 lang=python3
# @lcpr version=30204
#
# [1905] Count Sub Islands
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])

        def dfs(r, c):
            res = False if grid1[r][c] == 0 else True
            grid2[r][c] = 0 # mark as visited
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < m and 0 <= nc < n and grid2[nr][nc] == 1:
                    res &= dfs(nr, nc)
            return res

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    ans += dfs(i, j)
        return ans
# @lc code=end



#
# @lcpr case=start
# [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]\n[[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]\n[[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]\n
# @lcpr case=end

#

