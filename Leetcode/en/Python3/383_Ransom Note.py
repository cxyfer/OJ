# @algorithm @lc id=383 lang=python3 
# @title ransom-note


from en.Python3.mod.preImport import *
# @test("a","b")=false
# @test("aa","ab")=false
# @test("aa","aab")=true
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt1 = Counter(ransomNote)
        cnt2 = Counter(magazine)
        return all(cnt1[ch] <= cnt2[ch] for ch in cnt1)