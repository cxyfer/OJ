#
# @lc app=leetcode.cn id=1531 lang=python3
#
# [1531] 压缩字符串 II
#
from preImport import *
# @lc code=start
class Solution:
    """
        DP
        將問題轉化成從 n 個字元中選擇 n-k 個字元，使得壓縮後的長度最小
        dp[i][x] 表示從第 i 個字元開始，已選擇 x 個字元的最小壓縮長度
    """
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)   
        
        def calc(x): # 長度為 x 的相同字母壓縮後的長度
            if x == 1:
                return 1
            res = 0
            while x:
                x //= 10
                res += 1
            return res + 1

        # 1:1 翻譯成 recursive
        dp = [[float('inf')]*(n-k+1) for _ in range(n+1)]
        dp[n][n-k] = 0

        for i in range(n-1, -1, -1): # 從第 i 個字元開始，由後往前
            for x in range(n-k+1): # x 表示已選擇的字元數量
                cnt = 0
                dp[i][x] = dp[i+1][x] # 不選第 i 個字元
                for j in range(i, n):
                    if s[i] == s[j]:
                        cnt += 1
                        if x+cnt > n-k: # 如果已選擇的字元數量超過了 n-k，則不可行，跳出循環
                            break
                        dp[i][x] = min(dp[i][x], dp[j+1][x+cnt] + calc(cnt))
        return dp[0][0]

        @cache
        def dp(i, x): # dp(i, x) 表示從第 i 個字元開始，已選擇 x 個字元的最小壓縮長度
            if x > (n-k): # 如果選擇的字元數量超過了 n-k，則不可行，返回 inf
                return float('inf') 
            if i == n: # 終點，如果正好選擇 n-k 個，則是一個可行解，否則不可行，返回 inf
                return 0 if x == n-k else float('inf')

            res = dp(i+1, x) # 不選第 i 個字元
            cnt = 0 # 計算第 i 個字元後面有多少個相同的字元
            for j in range(i, n):
                if s[i] == s[j]:
                    cnt += 1
                    res = min(res, dp(j+1, x+cnt) + calc(cnt)) # 選擇 cnt 個相同的字元，壓縮後的長度為 calc(cnt)
            return res
        return dp(0, 0)
# @lc code=end
sol = Solution()
print(sol.getLengthOfOptimalCompression("aaabcccd",2)) # 4
print(sol.getLengthOfOptimalCompression("aabbaa",2)) # 2
print(sol.getLengthOfOptimalCompression("aaaaaaaaaaa",0)) # 3
print(sol.getLengthOfOptimalCompression("abbbbbbbbbba",2)) # 3