# @algorithm @lc id=97 lang=python3 
# @title interleaving-string


from en.Python3.mod.preImport import *
# @test("aabcc","dbbca","aadbbcbcac")=true
# @test("aabcc","dbbca","aadbbbaccc")=false
# @test("","","")=true
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # DP
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        # dp[i][j] = True if s1[:i] and s2[:j] can interleave s3[:i+j]
        dp = [[False] * (n+1) for _ in range(m+1)]
        # Base case
        dp[0][0] = True
        for i in range(1, m+1): # s3[:i] can be interleaved by s1[:i]
            if s1[i-1] == s3[i-1]:
                dp[i][0] = dp[i-1][0]
        for j in range(1, n+1): # s3[:j] can be interleaved by s2[:j]
            if s2[j-1] == s3[j-1]:
                dp[0][j] = dp[0][j-1]
        # Induction rule
        for i in range(1, m+1):
            for j in range(1, n+1):
                # s1[:i] and s2[:j] can interleave s3[:i+j]
                if i > 0 and s1[i-1] == s3[i+j-1]: # Transitions from dp[i-1][j]
                    dp[i][j] |= dp[i-1][j]
                if j > 0 and s2[j-1] == s3[i+j-1]: # Transitions from dp[i][j-1]
                    dp[i][j] |= dp[i][j-1]
        return dp[m][n]