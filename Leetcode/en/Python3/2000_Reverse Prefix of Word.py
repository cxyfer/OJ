# @algorithm @lc id=2128 lang=python3 
# @title reverse-prefix-of-word


from en.Python3.mod.preImport import *
# @test("abcdefd","d")="dcbaefd"
# @test("xyxzxe","z")="zxyxxe"
# @test("abcd","z")="abcd"
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        return word[:idx+1][::-1] + word[idx+1:]
        