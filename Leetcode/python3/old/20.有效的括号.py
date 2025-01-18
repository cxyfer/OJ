#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        st = [] # stack
        for ch in s:
            # push righr parenthese into stack when meet left parenthese
            if ch == '(':
                st.append(')')
            elif ch == '[':
                st.append(']')
            elif ch == '{':
                st.append('}') 
            # pop stack when meet right parenthese, and check if it matches
            else:
                if not st:
                    return False
                if ch != st.pop():
                    return False
        return True if not st else False
# @lc code=end

