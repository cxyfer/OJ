# @algorithm @lc id=742 lang=python3 
# @title to-lower-case


from en.Python3.mod.preImport import *
# @test("Hello")="hello"
# @test("here")="here"
# @test("LOVELY")="lovely"
class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = []
        for ch in s:
            if 'A' <= ch <= 'Z':
                ans.append(chr(ord(ch) + 32))
            else:
                ans.append(ch)
        return ''.join(ans)