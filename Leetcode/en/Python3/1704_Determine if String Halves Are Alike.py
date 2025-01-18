# @algorithm @lc id=1823 lang=python3 
# @title determine-if-string-halves-are-alike


from en.Python3.mod.preImport import *
# @test("book")=true
# @test("textbook")=false
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        def f(s: str) -> int:
            return sum([1 for ch in s if ch in "aeiouAEIOU"])
        return f(s[:n//2]) == f(s[n//2:])