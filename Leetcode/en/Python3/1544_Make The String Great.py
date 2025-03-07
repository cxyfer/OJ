# @algorithm @lc id=1666 lang=python3 
# @title make-the-string-great


from en.Python3.mod.preImport import *
# @test("leEeetcode")="leetcode"
# @test("abBAcC")=""
# @test("s")="s"
class Solution:
    def makeGood(self, s: str) -> str:
        st = []
        for ch in s:
            if st and abs(ord(ch) - ord(st[-1])) == 32:
                st.pop()
            else:
                st.append(ch)
        return ''.join(st)