#
# @lc app=leetcode id=20 lang=python3
# @lcpr version=30201
#
# [20] Valid Parentheses
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
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
            elif not st or ch != st.pop():
                return False
        return True if not st else False # 沒有多餘的左括號
# @lc code=end



#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "()[]{}"\n
# @lcpr case=end

# @lcpr case=start
# "(]"\n
# @lcpr case=end

#

