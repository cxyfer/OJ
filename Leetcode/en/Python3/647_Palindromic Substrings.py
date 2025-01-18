# @algorithm @lc id=647 lang=python3 
# @title palindromic-substrings


from en.Python3.mod.preImport import *
# @test("abc")=3
# @test("aaa")=6
class Solution:
    """
        Dynamic Programming
        dp[i][j] = True if s[i:j+1] is a palindrome
    """
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = 0
        for i in range(n): # 長度為 1 的palindrome substring
            dp[i][i] = True
            ans += 1
        for i in range(n-1): # 長度為 2 的palindrome substring
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans += 1
        for ln in range(3, n+1): # 長度>= 3 的palindrome substring
            for i in range(n-ln+1):
                j = i + ln - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    ans += 1
        return ans