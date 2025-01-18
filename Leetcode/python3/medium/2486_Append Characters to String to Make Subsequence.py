#
# @lc app=leetcode id=2486 lang=python3
# @lcpr version=30203
#
# [2486] Append Characters to String to Make Subsequence
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        i = j = 0
        while i < n and j < m:
            if s[i] == t[j]:
                j += 1
            i += 1
        return m - j
# @lc code=end



#
# @lcpr case=start
# "coaching"\n"coding"\n
# @lcpr case=end

# @lcpr case=start
# "abcde"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "z"\n"abcde"\n
# @lcpr case=end

#

