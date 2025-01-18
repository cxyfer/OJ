# @algorithm @lc id=2999 lang=python3 
# @title check-if-strings-can-be-made-equal-with-operations-i


from en.Python3.mod.preImport import *
# @test("abcd","cdab")=true
# @test("abcd","dacb")=false
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return Counter(s1[::2]) == Counter(s2[::2]) and Counter(s1[1::2]) == Counter(s2[1::2])
        