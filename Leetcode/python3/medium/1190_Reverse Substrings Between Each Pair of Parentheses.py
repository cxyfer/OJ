#
# @lc app=leetcode id=1190 lang=python3
# @lcpr version=30204
#
# [1190] Reverse Substrings Between Each Pair of Parentheses
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []
        for ch in s:
            if ch == ')':
                tmp = []
                while st and st[-1] != '(':
                    tmp.append(st.pop())
                st.pop() # pop '('
                st.extend(tmp)
            else:
                st.append(ch)
        return ''.join(st)
# @lc code=end



#
# @lcpr case=start
# "(abcd)"\n
# @lcpr case=end

# @lcpr case=start
# "(u(love)i)"\n
# @lcpr case=end

# @lcpr case=start
# "(ed(et(oc))el)"\n
# @lcpr case=end

#

