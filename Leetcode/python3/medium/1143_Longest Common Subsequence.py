#
# @lc app=leetcode id=1143 lang=python3
# @lcpr version=30204
#
# [1143] Longest Common Subsequence
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
max = lambda x, y: x if x > y else y
class Solution1:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        @cache
        def f(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            if s[i] == t[j]:
                return f(i - 1, j - 1) + 1
            return max(f(i - 1, j), f(i, j - 1))
        return f(m - 1, n - 1)

class Solution2:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        # f[i][j] 表示 s[:i] 和 t[:j] 的 LCS 長度
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:  # 可由左上方轉移
                    f[i][j] = f[i - 1][j - 1] + 1 
                else:  # 可由上方或左方轉移
                    f[i][j] = max(f[i - 1][j], f[i][j - 1])
        return f[m][n]

class Solution3:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        s = " " + s + " "
        t = " " + t + " "
        # f[i][j] 表示 s[:i] 和 t[:j] 的 LCS 長度
        f = [[0] * (n + 2) for _ in range(m + 2)]
        for i in range(m + 1):
            for j in range(n + 1):
                f[i + 1][j] = max(f[i + 1][j], f[i][j])
                f[i][j + 1] = max(f[i][j + 1], f[i][j])
                f[i + 1][j + 1] = max(f[i + 1][j + 1], f[i][j] + (s[i + 1] == t[j + 1]))
        return f[m][n]

# Solution = Solution1
Solution = Solution2
# Solution = Solution3
# @lc code=end

sol = Solution()
print(sol.longestCommonSubsequence("CGTTCGGAATG", "TCGAGTGC"))  # 6

#
# @lcpr case=start
# "abcde"\n"ace"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n"def"\n
# @lcpr case=end

#

