#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. Combination Math
2. Dynamic Programming
"""
# @lc code=start
MAX_N = 200
comb = [[1] * MAX_N for _ in range(MAX_N)]
for i in range(MAX_N):
    for j in range(1, i):
        comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j]

class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb[m + n - 2][m - 1]

class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        # 令 f(i, j) 為從 (i, j) 到 (m-1, n-1) 的路徑數
        @cache
        def f(x, y):
            if x == m - 1 and y == n - 1:
                return 1
            if x >= m or y >= n:
                return 0
            return f(x + 1, y) + f(x, y + 1)
        return f(0, 0)

class Solution3a:
    def uniquePaths(self, m: int, n: int) -> int:
        # 令 f(i, j) 為從 (0, 0) 到 (i, j) 的路徑數
        @cache
        def f(x, y):
            if x == 0 and y == 0:
                return 1
            if x < 0 or y < 0:
                return 0
            return f(x - 1, y) + f(x, y - 1)
        return f(m - 1, n - 1)

class Solution3b:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[0] * (n + 1) for _ in range(m + 1)]
        f[1][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1:
                    continue
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m][n]

class Solution3c:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [0] * (n + 1)
        f[1] = 1
        for i in range(1, m + 1):
            nf = [0] * (n + 1)
            for j in range(1, n + 1):
                nf[j] = nf[j - 1] + f[j]
            f = nf
        return f[n]
        
class Solution3d:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [0] * (n + 1)
        f[1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                f[j] = f[j - 1] + f[j]
        return f[n]

# Solution = Solution1
# Solution = Solution2
# Solution = Solution3a
# Solution = Solution3b
# Solution = Solution3c
Solution = Solution3d
# @lc code=end

