# @algorithm @lc id=387 lang=python3 
# @title first-unique-character-in-a-string


from en.Python3.mod.preImport import *
# @test("leetcode")=0
# @test("loveleetcode")=2
# @test("aabb")=-1
class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        for i, ch in enumerate(s):
            if cnt[ch] == 1:
                return i
        return -1