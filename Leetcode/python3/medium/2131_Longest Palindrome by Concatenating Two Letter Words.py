#
# @lc app=leetcode id=2131 lang=python3
#
# [2131] Longest Palindrome by Concatenating Two Letter Words
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt = Counter(words)
        ans = odd = 0
        for w, c in cnt.items():
            if w[0] == w[1]:
                ans += c // 2 * 2
                odd |= c & 1
            else:
                ans += min(c, cnt[w[1] + w[0]])
        return (ans + odd) * 2
# @lc code=end