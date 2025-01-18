# @algorithm @lc id=1371 lang=python3 
# @title minimum-remove-to-make-valid-parentheses


from en.Python3.mod.preImport import *
# @test("lee(t(c)o)de)")="lee(t(c)o)de"
# @test("a)b(c)d")="ab(c)d"
# @test("))((")=""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        st = []
        invalid = [False] * n
        for idx, ch in enumerate(s):
            if ch == '(':
                st.append(idx)
                invalid[idx] = True # 標記該下標的括號為無效
            elif ch == ')':
                if st:
                    invalid[st.pop()] = False # 取消標記
                else:
                    invalid[idx] = True # 標記該下標的括號為無效
        ans = [ch for idx, ch in enumerate(s) if not invalid[idx]]
        return ''.join(ans)