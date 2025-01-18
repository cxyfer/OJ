#
# @lc app=leetcode id=516 lang=python3
# @lcpr version=30204
#
# [516] Longest Palindromic Subsequence
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
1. 轉換為 LCS 問題
2. 區間 DP (Top-Down)
3. 區間 DP (Bottom-Up)
    - 寫法一：枚舉長度，由小區間到大區間
    - 寫法二：一比一翻譯，i 要由大到小，j 要由小到大
"""
class Solution1:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        t = s[::-1]
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n][n]

class Solution2:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        @cache
        def f(i, j):
            if i > j: return 0
            if i == j: return 1
            if s[i] == s[j]: # 兩端點相等，則可以都選
                return f(i + 1, j - 1) + 2
            return max(f(i + 1, j), f(i, j - 1)) # 兩端點不相等，則只能選擇其中一個
        return f(0, n - 1)

class Solution3a:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        f = [[0] * n for _ in range(n)]
        for i in range(n): # 初始化區間長度為 1 的值
            f[i][i] = 1
        for ln in range(2, n + 1): # 枚舉區間長度
            for i in range(n - ln + 1): # 枚舉區間左端點
                j = i + ln - 1 # 區間右端點
                if s[i] == s[j]:
                    f[i][j] = f[i + 1][j - 1] + 2
                else:
                    f[i][j] = max(f[i + 1][j], f[i][j - 1])
        return f[0][n - 1]

class Solution3b:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        f = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            f[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    f[i][j] = f[i + 1][j - 1] + 2
                else:
                    f[i][j] = max(f[i + 1][j], f[i][j - 1])
        return f[0][n - 1]

# class Solution(Solution1):
# class Solution(Solution2):
# class Solution(Solution3a):
class Solution(Solution3b):
    pass
# @lc code=end



#
# @lcpr case=start
# "bbbab"\n
# @lcpr case=end

# @lcpr case=start
# "cbbd"\n
# @lcpr case=end

#

