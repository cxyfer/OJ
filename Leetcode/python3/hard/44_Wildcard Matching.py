#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. Memoization
2. 查表法
3. 刷表法
"""
# @lc code=start
class Solution1:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        @cache
        def f(i: int, j: int) -> bool:
            if i < 0:  # s 已經匹配完，檢查 p 是否也匹配完或只剩下 *
                return j < 0 or all(p[k] == '*' for k in range(j + 1))
            if j < 0:  # s 還沒匹配完，p 已經匹配完，一定不匹配
                return False
            if p[j] == '*':  # * 可以匹配多個或 0 個字元
                return f(i - 1, j) or f(i, j - 1)
            if s[i] == p[j] or p[j] == '?':  # ? 可以匹配單個字元
                return f(i - 1, j - 1)
            return False
        return f(n - 1, m - 1)

class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        f = [[False] * (m + 1) for _ in range(n + 1)]
        f[0][0] = True
        for j in range(1, m + 1):
            f[0][j] = f[0][j - 1] and p[j - 1] == '*'
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j - 1] == '*':
                    f[i][j] = f[i - 1][j] or f[i][j - 1]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    f[i][j] = f[i - 1][j - 1]
        return f[n][m]

class Solution3:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        s = " " + s + " "
        p = " " + p + " "
        f = [[False] * (m + 2) for _ in range(n + 2)]
        f[0][0] = True
        for i in range(n + 1):
            for j in range(m + 1):
                if p[j + 1] == '*':
                    f[i + 1][j] |= f[i][j]
                    f[i][j + 1] |= f[i][j]
                elif p[j + 1] == '?' or s[i + 1] == p[j + 1]:
                    f[i + 1][j + 1] |= f[i][j]
        return f[n][m]

# Solution = Solution1
Solution = Solution2
# Solution = Solution3
# @lc code=end

