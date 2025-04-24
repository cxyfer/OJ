#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # f(i, j) 表示從 (i, j) 到 (m-1, n-1) 的方法數
        @cache
        def dfs(i, j):
            if i == m or j == n or obstacleGrid[i][j] == 1:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            return dfs(i + 1, j) + dfs(i, j + 1)
        return dfs(0, 0)

class Solution2a:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # f(i, j) 表示從 (0, 0) 到 (i, j) 的方法數
        @cache
        def dfs(i, j):
            if i < 0 or j < 0 or obstacleGrid[i][j] == 1:
                return 0
            if i == 0 and j == 0:
                return 1
            return dfs(i - 1, j) + dfs(i, j - 1)
        return dfs(m - 1, n - 1)
    
class Solution2b:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        f = [[0] * (n + 1) for _ in range(m + 1)]
        f[1][1] = 1 if obstacleGrid[0][0] == 0 else 0
        for i, row in enumerate(obstacleGrid, 1):
            for j, val in enumerate(row, 1):
                if i == 1 and j == 1:  # base case
                    continue
                if val == 1:
                    f[i][j] = 0
                else:
                    f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m][n]

class Solution2c:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        f = [0] * (n + 1)
        f[1] = 1
        for i, row in enumerate(obstacleGrid, 1):
            nf = [0] * (n + 1)
            for j, val in enumerate(row, 1):
                if val == 1:
                    nf[j] = 0
                else:
                    nf[j] = nf[j - 1] + f[j]
            f = nf
        return f[n]
    
class Solution2d:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        f = [0] * (n + 1)
        f[1] = 1
        for i, row in enumerate(obstacleGrid, 1):
            for j, val in enumerate(row, 1):
                if val == 1:
                    f[j] = 0
                else:
                    f[j] = f[j - 1] + f[j]
        return f[n]

# Solution = Solution1
# Solution = Solution2a
# Solution = Solution2b
# Solution = Solution2c
Solution = Solution2d
# @lc code=end

sol = Solution()
print(sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))  # 2
