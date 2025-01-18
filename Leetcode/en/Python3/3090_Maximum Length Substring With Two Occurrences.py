# @algorithm @lc id=3349 lang=python3 
# @title maximum-length-substring-with-two-occurrences


from en.Python3.mod.preImport import *
# @test("bcbbbcba")=4
# @test("aaaa")=2
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