# @algorithm @lc id=14 lang=python3 
# @title longest-common-prefix


from en.Python3.mod.preImport import *
# @test(["flower","flow","flight"])="fl"
# @test(["dog","racecar","car"])=""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = 0
        m, n = len(strs), len(strs[0])
        for i in range(n):
            ch = strs[0][i]
            for j in range(1, m):
                if i >= len(strs[j]) or strs[j][i] != ch:
                    return strs[0][:lcp]
            lcp += 1
        return strs[0][:lcp]