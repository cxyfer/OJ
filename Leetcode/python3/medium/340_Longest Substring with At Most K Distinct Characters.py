#
# @lc app=leetcode id=340 lang=python3
#
# [340] Longest Substring with At Most K Distinct Characters
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        ans = left = have = 0
        cnt = [0] * 128
        for right, ch in enumerate(s):
            cnt[ord(ch)] += 1
            if cnt[ord(ch)] == 1:
                have += 1
            while have > k:
                cnt[ord(s[left])] -= 1
                if cnt[ord(s[left])] == 0:
                    have -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
# @lc code=end

