#
# @lc app=leetcode id=409 lang=python3
# @lcpr version=30201
#
# [409] Longest Palindrome
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        ans = flag = 0
        for v in cnt.values():
            ans += v >> 1
            if v & 1:
                flag = 1
        return (ans << 1) + flag
# @lc code=end



#
# @lcpr case=start
# "abccccdd"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n
# @lcpr case=end

#

