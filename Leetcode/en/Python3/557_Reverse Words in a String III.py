# @algorithm @lc id=557 lang=python3 
# @title reverse-words-in-a-string-iii


from en.Python3.mod.preImport import *
# @test("Let's take LeetCode contest")="s'teL ekat edoCteeL tsetnoc"
# @test("God Ding")="doG gniD"
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([x[::-1] for x in s.split(' ')])
        