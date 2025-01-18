# @algorithm @lc id=459 lang=python3 
# @title repeated-substring-pattern


from en.Python3.mod.preImport import *
# @test("abab")=true
# @test("aba")=false
# @test("abcabcabcabc")=true
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s2 = s + s
        return s in s2[1:-1]