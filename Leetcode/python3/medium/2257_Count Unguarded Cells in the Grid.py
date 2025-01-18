#
# @lc app=leetcode id=2257 lang=python3
# @lcpr version=30204
#
# [2257] Count Unguarded Cells in the Grid
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[-1] * n for _ in range(m)]
        for x, y in guards:
            grid[x][y] = 1
        for x, y in walls:
            grid[x][y] = 2

        def dfs(x, y, dx, dy):
            if 0 <= x < m and 0 <= y < n and grid[x][y] not in [1, 2]:
                grid[x][y] = 3
                dfs(x + dx, y + dy, dx, dy)

        for x, y in guards:
            dfs(x, y + 1, 0, 1)
            dfs(x + 1, y, 1, 0)
            dfs(x, y - 1, 0, -1)
            dfs(x - 1, y, -1, 0)
        
        ans = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == -1:
                    ans += 1
        return ans
# @lc code=end

sol = Solution()
print(sol.countUnguarded(4, 6, [[0,0],[1,1],[2,3]], [[0,1],[2,2],[1,4]])) # 7

#
# @lcpr case=start
# 4\n6\n[[0,0],[1,1],[2,3]]\n[[0,1],[2,2],[1,4]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n3\n[[1,1]]\n[[0,1],[1,0],[2,1],[1,2]]\n
# @lcpr case=end

#

