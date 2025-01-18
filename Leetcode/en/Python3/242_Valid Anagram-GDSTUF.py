# @algorithm @lc id=242 lang=python3 
# @title valid-anagram


from en.Python3.mod.preImport import *
# @test("anagram","nagaram")=true
# @test("rat","car")=false
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt_s = Counter(s)
        cnt_t = Counter(t)
        return cnt_s == cnt_t