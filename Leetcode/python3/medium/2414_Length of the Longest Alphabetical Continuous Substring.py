#
# @lc app=leetcode id=2414 lang=python3
# @lcpr version=30204
#
# [2414] Length of the Longest Alphabetical Continuous Substring
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        n = len(s)
        ans = cur = 1
        for i in range(1, n):
            if ord(s[i]) - ord(s[i - 1]) == 1:
                cur += 1
                ans = max(ans, cur)
            else:
                cur = 1
        return ans
# @lc code=end



#
# @lcpr case=start
# "abacaba"\n
# @lcpr case=end

# @lcpr case=start
# "abcde"\n
# @lcpr case=end

#

