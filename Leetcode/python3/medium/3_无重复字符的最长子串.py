#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
from preImport import *
# @lc code=start
class Solution:
    """
        Sliding window
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        cnt = defaultdict(int)
        left = 0
        for right, ch in enumerate(s): # 枚舉右端點
            cnt[ch] += 1
            while (cnt[ch] > 1): # 縮小窗口(移動左端點)
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1) # 更新答案
        return ans
# @lc code=end

