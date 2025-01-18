# @algorithm @lc id=32 lang=python3 
# @title longest-valid-parentheses


from en.Python3.mod.preImport import *
# @test("(()")=2
# @test(")()())")=4
# @test("")=0
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n < 2: return 0
        ans = 0
        dp = [0] * n
        for i in range(1, n):
            if s[i] == ')':
                if i > 0 and s[i-1] == '(':
                    dp[i] = (dp[i-2] if i >= 2 else 0) + 2
                elif i - dp[i-1] > 0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] + (dp[i-dp[i-1]-2] if i-dp[i-1] >= 2 else 0) + 2
        return max(dp)