#
# @lc app=leetcode.cn id=3090 lang=python3
#
# [3090] 每个字符最多出现两次的最长子字符串
#
from preImport import *
# @lc code=start
class Solution:
    """
        Sliding Window
    """
    def maximumLengthSubstring(self, s: str) -> int:
        ans = 0
        cnt = Counter()
        left = 0
        for right, ch in enumerate(s):
            cnt[ch] += 1
            while cnt[ch] > 2: # 當前字元出現次數超過2次
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1) 
        return ans
# @lc code=end

