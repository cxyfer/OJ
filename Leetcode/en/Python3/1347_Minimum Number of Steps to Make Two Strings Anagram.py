# @algorithm @lc id=1469 lang=python3 
# @title minimum-number-of-steps-to-make-two-strings-anagram


from en.Python3.mod.preImport import *
# @test("bab","aba")=1
# @test("leetcode","practice")=5
# @test("anagram","mangaar")=0
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt1 = Counter(s)
        cnt2 = Counter(t)
        return sum([max(0, cnt1[k]-cnt2[k]) for k in cnt1.keys()])