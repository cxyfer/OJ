# @algorithm @lc id=3 lang=python3 
# @title longest-substring-without-repeating-characters


from en.Python3.mod.preImport import *
from collections import Counter
# @test("abcabcbb")=3
# @test("bbbbb")=1
# @test("pwwkew")=3
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