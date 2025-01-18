# @algorithm @lc id=2562 lang=python3 
# @title count-ways-to-build-good-strings


from en.Python3.mod.preImport import *
# @test(3,3,1,1)=8
# @test(2,3,1,2)=5
class Solution:
    """
        DP
        Similar to 70. Climbing Stairs
    """
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (high+1)
        dp[0] = 1
        for i in range(1, high+1):
            if i >= zero: # 可以在長度為 i-zero 的字串後面加上zero個0
                dp[i] += dp[i-zero]
            if i >= one: # 可以在長度為 i-one 的的字串後面加上one個1
                dp[i] += dp[i-one]
            dp[i] %= MOD
        return (sum(dp[low:high+1])) % MOD