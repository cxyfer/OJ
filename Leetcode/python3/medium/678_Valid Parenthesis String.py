#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
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
    
class Solution2:
    def checkValidString(self, s: str) -> bool:
        mn = mx = 0
        for ch in s:
            if ch == '(':
                mn += 1
                mx += 1
            elif ch == ')':
                mn = max(0, mn - 1)
                mx -= 1
                if mx < 0:
                    return False
            else:
                mn = max(0, mn - 1)
                mx += 1
        return mn == 0

# Solution = Solution1
Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.checkValidString("()")) #True
print(sol.checkValidString("(*)")) #True
print(sol.checkValidString("(*))")) #True
s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
print(sol.checkValidString(s)) # False