#
# @lc app=leetcode.cn id=678 lang=python3
#
# [678] 有效的括号字符串
#
from preImport import *
# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        st = [] # stack for index of '(' and ')'
        st_s = [] # stack for index of '*'
        for i, ch in enumerate(s):
            if ch == '(':
                st.append(i)
            elif ch == ')':
                if st:
                    st.pop()
                elif st_s:
                    st_s.pop()
                else:
                    return False
            else:
                st_s.append(i)
        if len(st) > len(st_s):
            return False
        while st and st_s:
            if st.pop() > st_s.pop():
                return False
        return True
# @lc code=end
sol = Solution()
# print(sol.checkValidString("()")) #True
print(sol.checkValidString("(*)")) #True
# print(sol.checkValidString("(*))")) #True
s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
print(sol.checkValidString(s)) # False