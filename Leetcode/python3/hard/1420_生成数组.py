#
# @lc app=leetcode.cn id=1420 lang=python3
#
# [1420] 生成数组
#
from preImport import *
# @lc code=start
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        if k == 0: # 不存在搜尋代價為 0 的Array
            return 0
        # dp[i][s][j] 表示長度為 i，搜索代價為 s，最大值為 j 的Array的數量
        dp = [[[0] * (m + 1) for _ in range(k + 1)] for __ in range(n + 1)]
        MOD = 10**9 + 7
        # base case，所有長度為 1 的Array的搜尋代價都為 1
        for j in range(1, m + 1):
            dp[1][1][j] = 1
        for i in range(2, n + 1):
            for s in range(1, min(k, i) + 1): # 搜尋代價不會超過Array長度
                for j in range(1, m + 1): # 最大值
                    # case 1: 沒有新的最大值，搜尋代價不變
                    # 從長度為 i - 1 的情況轉移，且最後一個數字有 j 種選擇
                    dp[i][s][j] = dp[i - 1][s][j] * j
                    # case 2: 第 i 個數字是新的最大值，搜尋代價加 1
                    # 從長度為 i - 1，搜尋代價為 s - 1 的，最大值為 1~j 的情況轉移
                    for j0 in range(1, j):
                        dp[i][s][j] += dp[i - 1][s - 1][j0]
                    dp[i][s][j] %= MOD
        # 最終的答案是所有 dp[n][k][..] 的和，即Array長度為 n，搜尋代價為 k，最大值任意
        return sum(dp[n][k][j] for j in range(1, m + 1)) % MOD
# @lc code=end

