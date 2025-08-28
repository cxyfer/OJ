#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        @cache
        def dfs(i: int, j: int) -> int:
            if n - i < m - j:  # 剪枝，s 剩下的比 t 剩下的多，一定不合法
                return 0
            if j == m:
                return 1
            res = dfs(i + 1, j)
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
            return res
        return dfs(0, 0)

class Solution2a:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        @cache
        def dfs(i: int, j: int) -> int:
            if i < j:  # 剪枝，s 剩下的比 t 剩下的多，一定不合法
                return 0
            if j < 0:
                return 1
            res = dfs(i - 1, j)
            if s[i] == t[j]:
                res += dfs(i - 1, j - 1)
            return res
        return dfs(n - 1, m - 1)

class Solution2b:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        f = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            f[i][0] = 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                f[i][j] = f[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    f[i][j] += f[i - 1][j - 1]
        return f[n][m]

class Solution2c:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        f = [[0] * (m + 1) for _ in range(2)]
        f[0][0] = f[1][0] = 1
        for i in range(1, n + 1):
            cur, pre = i & 1, (i - 1) & 1
            for j in range(1, m + 1):
                f[cur][j] = f[pre][j]
                if s[i - 1] == t[j - 1]:
                    f[cur][j] += f[pre][j - 1]
        return f[n & 1][m]

# Solution = Solution1
Solution = Solution2a
# Solution = Solution2b
# Solution = Solution2c
# @lc code=end

