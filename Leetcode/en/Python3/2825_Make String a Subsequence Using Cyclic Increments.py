# @algorithm @lc id=3018 lang=python3 
# @title make-string-a-subsequence-using-cyclic-increments


from en.Python3.mod.preImport import *
# @test("abc","ad")=true
# @test("zc","ad")=true
# @test("ab","d")=false
from math import inf
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        index = 0
        n = len(str2)
        for char in str1:
            if index < n and (ord(str2[index]) - ord(char)) % 26 <= 1:
                index += 1
        return index == n