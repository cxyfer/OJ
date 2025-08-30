#
# @lc app=leetcode id=980 lang=python3
#
# [980] Unique Paths III
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        tot = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 0:
                    tot += 1
                elif x == 1:
                    sx, sy = i, j

        ans = cnt = 0
        def dfs(i, j):
            nonlocal cnt, ans
            if grid[i][j] == 2:
                nonlocal ans
                ans += cnt == tot + 1
                return
            cnt += 1
            grid[i][j] = -1
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = i + dx, j + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m or grid[nx][ny] == -1:
                    continue
                dfs(nx, ny)
            cnt -= 1
            grid[i][j] = 0

        dfs(sx, sy)
        return ans
# @lc code=end

sol = Solution()
print(sol.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))  # 2
# print(sol.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]]))  # 4
# print(sol.uniquePathsIII([[0,1],[2,0]]))  # 0
