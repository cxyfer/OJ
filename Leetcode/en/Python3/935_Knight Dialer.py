# @algorithm @lc id=972 lang=python3 
# @title knight-dialer


from en.Python3.mod.preImport import *
# @test(1)=10
# @test(2)=20
# @test(3131)=136006598
class Solution(object):
    """
        Dynamic Programming
    """
    def knightDialer(self, N):
        MOD = 10**9 + 7
        pre = {
                0: [4, 6],
                1: [6, 8],
                2: [7, 9],
                3: [4, 8],
                4: [0, 3, 9],
                5: [],
                6: [0, 1, 7],
                7: [2, 6],
                8: [1, 3],
                9: [2, 4] 
            }

        dp = [[0] * 10 for _ in range(N)]
        for x in range(10):
            dp[0][x] = 1
        for i in range(1, N):
            for x in range(10):
                dp[i][x] = sum(dp[i-1][y] for y in pre[x]) % MOD
        return sum(dp[N-1]) % MOD