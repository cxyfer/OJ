# @algorithm @lc id=1777 lang=python3 
# @title determine-if-two-strings-are-close


from en.Python3.mod.preImport import *
# @test("abc","bca")=true
# @test("a","aa")=false
# @test("cabbba","abbccc")=true
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        cnt1 = Counter(word1)
        cnt2 = Counter(word2)
        return sorted(cnt1.keys()) == sorted(cnt2.keys()) and sorted(cnt1.values()) == sorted(cnt2.values())
