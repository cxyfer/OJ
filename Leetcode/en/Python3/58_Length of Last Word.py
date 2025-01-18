# @algorithm @lc id=58 lang=python3 
# @title length-of-last-word


from en.Python3.mod.preImport import *
# @test("Hello World")=5
# @test("   fly me   to   the moon  ")=4
# @test("luffy is still joyboy")=6
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # return len(s.strip().split(' ')[-1])
        ans = cur = 0
        for ch in s:
            if ch == ' ':
                ans = cur if cur != 0 else ans
                cur = 0
            else:
                cur += 1
        return cur if cur != 0 else ans

        