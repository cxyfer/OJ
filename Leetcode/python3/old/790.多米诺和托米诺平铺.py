#
# @lc app=leetcode.cn id=790 lang=python3
#
# [790] 多米诺和托米诺平铺
#

# @lc code=start
class Solution:
    """
        Tromino 的情況比較難想到，參考靈神的圖示
        dp[3] = dp[2] + dp[1] + 2
        dp[4] = dp[3] + dp[2] + (dp[1] + 1) * 2
        dp[5] = dp[4] + dp[3] + (dp[2] + dp[1] + 1) * 2
        ...
        dp[n-1] = dp[n-2] + dp[n-3] + (dp[n-4] + ... + 1) * 2
        dp[n] = dp[n-1] + dp[n-2] + (dp[n-3] + dp[n-4] + ... + 1) * 2
        兩式相減得到 dp[n] = dp[n-1] * 2 + dp[n-3]
    """
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        if n == 0: return 1
        if n <= 2: return n
        dp = [0] * (n+1)
        dp[0], dp[1], dp[2] = 1, 1, 2
        for i in range(3, n+1):
            dp[i] = (dp[i-1] * 2 + dp[i-3]) % MOD
        return dp[n]
# @lc code=end
sol = Solution()
print(sol.numTilings(4)) # 11
