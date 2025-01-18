# @algorithm @lc id=1885 lang=python3 
# @title count-number-of-homogenous-substrings


from en.Python3.mod.preImport import *
# @test("abbcccaa")=13
# @test("xy")=2
# @test("zzzzz")=15
class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        ans = l = 1
        for i in range(1, n):
            if s[i] == s[i-1]:
                l += 1
            else:
                l = 1
            ans += l % MOD
        return ans % MOD