# @algorithm @lc id=10 lang=python3 
# @title regular-expression-matching


from en.Python3.mod.preImport import *
# @test("aa","a")=false
# @test("aa","a*")=true
# @test("ab",".*")=true
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        