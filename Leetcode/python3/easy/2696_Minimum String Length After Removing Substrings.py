#
# @lc app=leetcode id=2696 lang=python3
# @lcpr version=30204
#
# [2696] Minimum String Length After Removing Substrings
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minLength(self, s: str) -> int:
        st = []
        for ch in s:
            if len(st) and (st[-1] == "A" and ch == "B" or st[-1] == "C" and ch == "D"):
                st.pop()
            else:
                st.append(ch)
        return len(st)
# @lc code=end



#
# @lcpr case=start
# "ABFCACDB"\n
# @lcpr case=end

# @lcpr case=start
# "ACBBD"\n
# @lcpr case=end

#

