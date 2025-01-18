#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    """
        Dynamic Programming
        dp[i][j] 表示 s[i..j] 是否為回文串
    """
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1: return s
        dp = [[False] * n for _ in range(n)]
        for i in range(n): # 初始化：所有長度為1的子串都是回文串
            dp[i][i] = True
        ans = 1 # 最長回文子串長度
        st = 0 # 最長回文子串起點
        for l in range(2, n+1): # 長度為2~n的子串
            for i in range(n-l+1): # 起點為0~n-l
                j = i + l - 1 # 終點為i+l-1
                if s[i] == s[j]: # 頭尾相等
                    if l == 2 or dp[i+1][j-1]: # 長度為2的子串 or 去掉頭尾之後還是回文串
                        dp[i][j] = True
                        if l > ans: # 更新最長回文子串長度和起點
                            ans = l
                            st = i
        return s[st:st+ans]
# @lc code=end

