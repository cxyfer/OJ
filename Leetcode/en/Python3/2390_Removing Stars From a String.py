# @algorithm @lc id=2470 lang=python3 
# @title removing-stars-from-a-string


from en.Python3.mod.preImport import *
# @test("leet**cod*e")="lecoe"
# @test("erase*****")=""
class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for c in s:
            if c == '*':
                if st: st.pop()
            else:
                st.append(c)
        return ''.join(st)