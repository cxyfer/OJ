# @algorithm @lc id=874 lang=python3 
# @title backspace-string-compare


from en.Python3.mod.preImport import *
# @test("ab#c","ad#c")=true
# @test("ab##","c#d#")=true
# @test("a#c","b")=false
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # return self.solve1(s, t)
        return self.solve2(s, t)
    """
        1. Stack
    """
    def solve1(self, s: str, t: str) -> bool:
        def build(s: str) -> str:
            st = []
            for ch in s:
                if ch == "#":
                    if st: st.pop()
                else:
                    st.append(ch)
            return "".join(st)
        return build(s) == build(t)
    """
        2. Two Pointers (from end to starts)
        i,j 分別指向真正要比對的字元，即將可刪除的字元跳過
    """
    def solve2(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1 # 指向真正要比對的字元
        skipS = skipT = 0 # 跳過的字元數

        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == "#":
                    skipS += 1
                elif skipS > 0:
                    skipS -= 1
                else:
                    break
                i -= 1
            while j >= 0:
                if t[j] == "#":
                    skipT += 1
                elif skipT > 0:
                    skipT -= 1
                else:
                    break
                j -= 1
            # 找出真正需要比對的字元後開始比對
            if i >= 0 and j >= 0:
                if s[i] != t[j]: #字元不同
                    return False
            elif (i >= 0 and j < 0) or (i < 0 and j >= 0): # 長度不同
                return False
            i -= 1
            j -= 1
        return True