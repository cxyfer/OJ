# @algorithm @lc id=3174 lang=python3 
# @title minimum-number-of-changes-to-make-binary-string-beautiful


from en.Python3.mod.preImport import *
# @test("1001")=2
# @test("10")=1
# @test("0000")=0
class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n//2):
            if s[2*i] != s[2*i+1]:
                ans += 1
        return ans
    
