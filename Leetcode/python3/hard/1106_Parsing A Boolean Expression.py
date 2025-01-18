#
# @lc app=leetcode id=1106 lang=python3
# @lcpr version=30204
#
# [1106] Parsing A Boolean Expression
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        st = []
        for ch in expression:
            if ch == ',':
                continue
            if ch in "(!&|":
                st.append(ch)
                continue
            elif ch in "tf":
                st.append(ch == 't')
                continue
            elif ch == ')':
                t = f = 0
                while st[-1] != '(':
                    if st.pop() == True:
                        t += 1
                    else:
                        f += 1
                st.pop()
                op = st.pop()
                if op == '&':
                    st.append(f == 0)
                elif op == '|':
                    st.append(t > 0)
                elif op == '!':
                    st.append(f == 1)
        return st[-1]
# @lc code=end



#
# @lcpr case=start
# "&(|(f))"\n
# @lcpr case=end

# @lcpr case=start
# "|(f,f,f,t)"\n
# @lcpr case=end

# @lcpr case=start
# "!(&(f,t))"\n
# @lcpr case=end

#

