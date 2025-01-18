# @algorithm @lc id=1208 lang=python3 
# @title maximum-nesting-depth-of-two-valid-parentheses-strings


from en.Python3.mod.preImport import *
# @test("(()())")=[0,1,1,1,1,0]
# @test("()(())()")=[0,0,0,1,1,0,1,1]
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        