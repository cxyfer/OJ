# @algorithm @lc id=1737 lang=python3 
# @title maximum-nesting-depth-of-the-parentheses


from en.Python3.mod.preImport import *
# @test("(1+(2*3)+((8)/4))+1")=3
# @test("(1)+((2))+(((3)))")=3
class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        cnt = 0
        for ch in s:
            if ch == '(':
                cnt += 1
                ans = max(ans, cnt)
            elif ch == ')':
                cnt -= 1
        return ans