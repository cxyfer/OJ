#
# @lc app=leetcode id=2825 lang=python3
# @lcpr version=30204
#
# [2825] Make String a Subsequence Using Cyclic Increments
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        m, n = len(str1), len(str2)
        j = 0
        for i in range(m):
            if j < n and (ord(str2[j]) - ord(str1[i])) % 26 <= 1:
                j += 1
        return j == n
# @lc code=end
#
# @lcpr case=start
# "abc"\n"ad"\n
# @lcpr case=end

# @lcpr case=start
# "zc"\n"ad"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n"d"\n
# @lcpr case=end

#

