2#
# @lc app=leetcode.cn id=1269 lang=python3
#
# [1269] 停在原地的方案数
#

# @lc code=start
class Solution:
    """
        Dynamic Programming
    """
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        # dp[i][j] 表示經過i步後，指針位於j的方案數
        max_j = min(arrLen - 1, steps) # 最遠能走到的位置
        dp = [[0] * (max_j + 1) for _ in range(steps + 1)]
        dp[0][0] = 1

        for i in range(1, steps + 1):
            for j in range(0, max_j + 1):
                dp[i][j] = dp[i - 1][j] # 不移動
                if j - 1 >= 0: # 向左移動
                    dp[i][j] += dp[i - 1][j - 1]
                if j + 1 <= max_j: # 向右移動
                    dp[i][j] += dp[i - 1][j + 1]
                dp[i][j] %= MOD
        return dp[steps][0]
# @lc code=end

