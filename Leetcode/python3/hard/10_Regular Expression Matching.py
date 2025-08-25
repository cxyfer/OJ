#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
Extended from 44. Wildcard Matching

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
            if i < 0:  # s 已經匹配完，檢查 p 是否也匹配完或只剩下 a*b*c*...
                return j < 0 or (p[j] == '*' and f(i, j - 2))
            if j < 0:  # s 還沒匹配完，p 已經匹配完，一定不匹配
                return False
            if p[j] == '*':  # * 可以匹配 0 個或多個前置字元
                return f(i, j - 2) or ((s[i] == p[j - 1] or p[j - 1] == '.') and f(i - 1, j))
            if s[i] == p[j] or p[j] == '.':  # . 可以匹配單個字元
                return f(i - 1, j - 1)
            return False
        return f(n - 1, m - 1)

class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        s = " " + s
        p = " " + p
        f = [[False] * (m + 1) for _ in range(n + 1)]
        f[0][0] = True
        for j in range(2, m + 1):
            f[0][j] = f[0][j - 2] and p[j] == '*'
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j] == '*':
                    f[i][j] = f[i][j - 2] or ((s[i] == p[j - 1] or p[j - 1] == '.') and f[i - 1][j])
                elif p[j] == '.' or s[i] == p[j]:
                    f[i][j] = f[i - 1][j - 1]
        return f[n][m]

class Solution3:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        s = " " + s + " "
        p = " " + p + "  "
        f = [[False] * (m + 3) for _ in range(n + 2)]
        f[0][0] = True
        for i in range(n + 1):
            for j in range(m + 1):
                if p[j + 2] == '*':
                    f[i][j + 2] |= f[i][j]
                    f[i + 1][j] |= (s[i + 1] == p[j + 1] or p[j + 1] == '.') and f[i][j]
                f[i + 1][j + 1] |= (s[i + 1] == p[j + 1] or p[j + 1] == '.') and f[i][j]
        return f[n][m]

Solution = Solution1
# Solution = Solution2
# Solution = Solution3
# @lc code=end