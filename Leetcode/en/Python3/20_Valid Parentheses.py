# @algorithm @lc id=20 lang=python3 
# @title valid-parentheses


from en.Python3.mod.preImport import *
# @test("()")=true
# @test("()[]{}")=true
# @test("(]")=false
class Solution:
    """
        Stack
    """
    def isValid(self, s: str) -> bool:
        st = []
        for ch in s:
            # push righr parenthese into stack when meet left parenthese
            if ch == "(":
                st.append(")")
            elif ch == "[":
                st.append("]")
            elif ch == "{":
                st.append("}")
            # pop stack when meet right parenthese, and check if it matches
            else:
                if not st or ch != st.pop():
                    return False
        return True if not st else False # 沒有多餘的左括號