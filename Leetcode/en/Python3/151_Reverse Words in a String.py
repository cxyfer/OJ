# @algorithm @lc id=151 lang=python3 
# @title reverse-words-in-a-string


from en.Python3.mod.preImport import *
# @test("the sky is blue")="blue is sky the"
# @test("  hello world  ")="world hello"
# @test("a good   example")="example good a"
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([word for word in s.split(" ")[::-1] if word])
        