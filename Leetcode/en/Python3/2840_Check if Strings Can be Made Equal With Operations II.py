# @algorithm @lc id=2978 lang=python3 
# @title check-if-strings-can-be-made-equal-with-operations-ii


from en.Python3.mod.preImport import *
# @test("abcdba","cabdab")=true
# @test("abe","bea")=false
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        return Counter(s1[::2]) == Counter(s2[::2]) and Counter(s1[1::2]) == Counter(s2[1::2])