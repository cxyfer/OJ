# @algorithm @lc id=1894 lang=python3 
# @title merge-strings-alternately


from en.Python3.mod.preImport import *
# @test("abc","pqr")="apbqcr"
# @test("ab","pqrs")="apbqrs"
# @test("abcd","pq")="apbqcd"
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        ans = ""
        for i in range(max(m, n)):
            if i < m:
                ans += word1[i]
            if i < n:
                ans += word2[i]
        return ans