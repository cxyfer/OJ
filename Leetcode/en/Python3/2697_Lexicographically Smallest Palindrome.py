# @algorithm @lc id=2816 lang=python3 
# @title lexicographically-smallest-palindrome


from en.Python3.mod.preImport import *
# @test("egcfe")="efcfe"
# @test("abcd")="abba"
# @test("seven")="neven"
class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)
        res = list(s)
        for i in range((n+1)//2):
            if s[i] != s[n-1-i]:
                res[i] = res[n-1-i] = min(s[i], s[n-1-i])
        return ''.join(res)