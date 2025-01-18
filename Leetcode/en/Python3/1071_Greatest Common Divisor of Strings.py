# @algorithm @lc id=1146 lang=python3 
# @title greatest-common-divisor-of-strings


from en.Python3.mod.preImport import *
# @test("ABCABC","ABC")="ABC"
# @test("ABABAB","ABAB")="AB"
# @test("LEET","CODE")=""
import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        candidate_len = math.gcd(len(str1), len(str2))
        candidate = str1[:candidate_len]
        if str1 + str2 == str2 + str1:
            return candidate
        return ''