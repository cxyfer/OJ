#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2: return s
        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]
        # 初始化：所有長度為1的子串都是回文串
        for i in range(n):
            dp[i][i] = True
        max_len = 1
        start = 0
        # 開始填表
        for j in range(1, n):
            for i in range(j):
                # 狀態轉移方程
                # 如果頭尾相等且去掉頭尾之後還是回文串，那麼這個子串也是回文串
                if s[i] == s[j]:
                    if j - i < 3: # 長度為2或3的子串
                        dp[i][j] = True
                    else:
                        if dp[i+1][j-1]:
                            dp[i][j] = True
                # 更新最長回文子串的長度和起點
                if dp[i][j]:
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        start = i
        return s[start:start+max_len]
# @lc code=end

