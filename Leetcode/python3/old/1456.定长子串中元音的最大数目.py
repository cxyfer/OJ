#
# @lc app=leetcode.cn id=1456 lang=python3
#
# [1456] 定长子串中元音的最大数目
#

# @lc code=start
class Solution:
    """
        Sliding window
    """
    def maxVowels(self, s: str, k: int) -> int:
        ans = cur = sum(1 for ch in s[:k] if ch in 'aeiou')
        for idx in range(k, len(s)):
            if s[idx] in 'aeiou':
                cur += 1
            if s[idx-k] in 'aeiou':
                cur -= 1
            ans = max(ans, cur)
        return ans
# @lc code=end

