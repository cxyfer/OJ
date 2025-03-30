#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        for ch in s:
            if st and st[-1] == ch:
                st.pop()
            else:
                st.append(ch)
        return "".join(st)
# @lc code=end

