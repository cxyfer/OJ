# @algorithm @lc id=72 lang=python3 
# @title edit-distance


from en.Python3.mod.preImport import *
# @test("horse","ros")=3
# @test("intention","execution")=5
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m == 0 or n == 0: # 有一個為空
            return m + n
        # dp[i][j] 表示將 word1的前i個字元 轉換成 word2的前j個字元 所需的最少操作次數
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        # 初始化
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]: # 上一個字元相同
                    dp[i][j] = dp[i-1][j-1]
                else: # 上一個字元不同
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1 # 刪除 / 插入 / 替換
        return dp[m][n]