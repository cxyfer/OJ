# @algorithm @lc id=91 lang=python3 
# @title decode-ways


from en.Python3.mod.preImport import *
# @test("12")=2
# @test("226")=3
# @test("06")=0
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(2, n+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if s[i-2] != '0' and int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2] 
        return dp[-1]