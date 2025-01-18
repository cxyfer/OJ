#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#
from preImport import *
# @lc code=start
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
# @lc code=end
sol = Solution()

print(sol.evalRPN(["2","1","+","3","*"])) # 9 
print(sol.evalRPN(["4","13","5","/","+"])) # 6
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])) # 22
["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])) # 22
