#
# @lc app=leetcode id=2852 lang=python3
# @lcpr version=30204
#
# [2852] Sum of Remoteness of All Cells
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        n = len(grid)
        tot = sum(val for row in grid for val in row if val > 0)
        vis = [[False] * n for _ in range(n)]
        ans = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == -1 or vis[i][j]:
                    continue
                s = cnt = 0
                vis[i][j] = True
                q = deque([(i, j)])
                while q:
                    x, y = q.popleft()
                    s += grid[x][y]
                    cnt += 1
                    for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and not vis[nx][ny] and grid[nx][ny] > 0:
                            vis[nx][ny] = True
                            q.append((nx, ny))
                ans += (tot - s) * cnt
        return ans
# @lc code=end

sol = Solution()
print(sol.sumRemoteness([[-1,1,-1],[5,-1,4],[-1,3,-1]]))

#
# @lcpr case=start
# [[-1,1,-1],[5,-1,4],[-1,3,-1]]\n
# @lcpr case=end

# @lcpr case=start
# [[-1,3,4],[-1,-1,-1],[3,-1,-1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1]]\n
# @lcpr case=end

#

