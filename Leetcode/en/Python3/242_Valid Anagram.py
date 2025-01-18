# @algorithm @lc id=242 lang=python3 
# @title valid-anagram


from en.Python3.mod.preImport import *
# @test("anagram","nagaram")=true
# @test("rat","car")=false
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        return Counter(s) == Counter(t)