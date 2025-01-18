#
# @lc app=leetcode.cn id=1155 lang=python3
#
# [1155] 掷骰子等于目标和的方法数
#

# @lc code=start
class Solution:
    """
        DP
        令 dp[i][j] 為擲 i 顆骰子和為 j 的方法數
    """
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for j in range(1, min(k, target) + 1): # 初始化一顆骰子的情況
            dp[1][j] = 1
        for i in range(2, n+1): # 骰子數
            for j in range(1, target+1): # 考慮和為j的情況
                for x in range(1, k+1): # 第i個骰子的點數為x
                    if j - x < 0:
                        break
                    dp[i][j] += dp[i-1][j-x] % MOD # 從前 i-1 顆骰子和為 j-x 的情況轉移過來
        return dp[n][target] % MOD
# @lc code=end
sol = Solution()
print(sol.numRollsToTarget(1,6,3)) # 1
print(sol.numRollsToTarget(2,6,7)) # 6
print(sol.numRollsToTarget(30,30,500)) # 222616187
