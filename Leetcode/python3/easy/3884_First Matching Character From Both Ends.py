#
# @lc app=leetcode id=3884 lang=python3
#
# [3884] First Matching Character From Both Ends
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        n = len(s)
        for i in range(n // 2 + 1):
            if s[i] == s[n - i - 1]:
                return i
        return -1
# @lc code=end

