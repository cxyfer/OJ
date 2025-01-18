# @algorithm @lc id=807 lang=python3 
# @title custom-sort-string


from en.Python3.mod.preImport import *
# @test("cba","abcd")="cbad"
# @test("bcafg","abcd")="bcad"
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1
        ans = ''
        for ch in order:
            ans += ch * cnt[ord(ch) - ord('a')]
            cnt[ord(ch) - ord('a')] = 0
        for i in range(26):
            ans += chr(i + ord('a')) * cnt[i]
        return ans