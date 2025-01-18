# @algorithm @lc id=394 lang=python3 
# @title decode-string


from en.Python3.mod.preImport import *
# @test("3[a]2[bc]")="aaabcbc"
# @test("3[a2[c]]")="accaccacc"
# @test("2[abc]3[cd]ef")="abcabccdcdcdef"
class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        num = 0
        cur = ""
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '[':
                st.append((num, cur))
                num = 0
                cur = ""
            elif ch == ']':
                n, tmp = st.pop()
                cur = tmp + cur * n
            else:
                cur += ch
            # print(ch, st, cur)
        return cur