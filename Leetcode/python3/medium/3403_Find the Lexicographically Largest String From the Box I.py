#
# @lc app=leetcode id=3403 lang=python3
# @lcpr version=30204
#
# [3403] Find the Lexicographically Largest String From the Box I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def answerString(self, s: str, k: int) -> str:
        if k == 1: return s
        n = len(s)
        ln = n - k + 1
        return max(s[i:i+ln] for i in range(n))
# @lc code=end



#
# @lcpr case=start
# "dbca"\n2\n
# @lcpr case=end

# @lcpr case=start
# "gggg"\n4\n
# @lcpr case=end

#

