# @algorithm @lc id=1332 lang=python3 
# @title count-vowels-permutation


from en.Python3.mod.preImport import *
# @test(1)=5
# @test(2)=10
# @test(5)=68
class Solution:
    """
        Dynamic Programming
        dp[i][j] 表示長度為 i 的字串，以 第j個母音 結尾的數目
    """
    def countVowelPermutation(self, n: int) -> int:
        return self.solve1(n)
    def solve1(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * 5 for _ in range(n+1)]
        for j in range(5):
            dp[1][j] = 1
        for i in range(2, n+1):
            dp[i][0] = dp[i-1][1] + dp[i-1][2] + dp[i-1][4] # a 前面可以是 e, i, u
            dp[i][1] = dp[i-1][0] + dp[i-1][2] # e 前面可以是 a, i
            dp[i][2] = dp[i-1][1] + dp[i-1][3] # i 前面可以是 e, o
            dp[i][3] = dp[i-1][2] # o 前面可以是 i
            dp[i][4] = dp[i-1][2] + dp[i-1][3] # u 前面可以是 i, o
            for j in range(5):
                dp[i][j] %= MOD
        return sum(dp[n]) % (10**9 + 7)
    def solve2(self, n: int) -> int:
        MOD = 10**9 + 7
        pre, cur = [1] * 5, [0] * 5
        for i in range(2, n+1):
            cur[0] = pre[1] + pre[2] + pre[4] # a 前面可以是 e, i, u
            cur[1] = pre[0] + pre[2] # e 前面可以是 a, i
            cur[2] = pre[1] + pre[3] # i 前面可以是 e, o
            cur[3] = pre[2] # o 前面可以是 i
            cur[4] = pre[2] + pre[3] # u 前面可以是 i, o
            pre = cur[:]
            for j in range(5):
                cur[j] %= MOD
        return sum(pre) % MOD