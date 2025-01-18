#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
from en.Python3.mod.preImport import *
from collections import Counter
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # left = -1
        # window = {}
        # ans = 0
        # for right in range(len(s)):
        #     if s[right] in window:
        #         left = max(left, window[s[right]])
        #     window[s[right]] = right
        #     ans = max(ans, right - left)
        # return ans
        
        # Sliding window, two pointers
        ans = 0
        cnt = Counter()
        left = 0
        for right, char in enumerate(s):
            cnt[char] += 1
            while cnt[char] > 1: # 縮小窗口
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
# @lc code=end

