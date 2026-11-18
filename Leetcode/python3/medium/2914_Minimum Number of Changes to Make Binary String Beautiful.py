#
# @lc app=leetcode id=2914 lang=python3
#
# [2914] Minimum Number of Changes to Make Binary String Beautiful
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(0, n, 2):
            ans += (s[i] != s[i + 1])
        return ans
# @lc code=end

