# @algorithm @lc id=150 lang=python3 
# @title evaluate-reverse-polish-notation


from en.Python3.mod.preImport import *
# @test(["2","1","+","3","*"])=9
# @test(["4","13","5","/","+"])=6
# @test(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])=22
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                a = int(st.pop())
                b = int(st.pop())
                if token == '+':
                    st.append(b + a)
                elif token == '-':
                    st.append(b - a)
                elif token == '*':
                    st.append(b * a)
                elif token == '/':
                    st.append(int(b / a))
            else:
                st.append(int(token))
        return st[-1]