#
# @lc app=leetcode id=3174 lang=python3
# @lcpr version=30203
#
# [3174] Clear Digits
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def clearDigits(self, s: str) -> str:
        st = []
        for ch in s:
            if ch.isdigit():
                st.pop()
            else:
                st.append(ch)
        return ''.join(st)
# @lc code=end



#
# @lcpr case=start
# "abc"\n
# @lcpr case=end

# @lcpr case=start
# "cb34"\n
# @lcpr case=end

#

