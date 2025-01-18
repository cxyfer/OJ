# @algorithm @lc id=32 lang=python3 
# @title longest-valid-parentheses


from en.Python3.mod.preImport import *
# @test("(()")=2
# @test(")()())")=4
# @test("")=0
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        