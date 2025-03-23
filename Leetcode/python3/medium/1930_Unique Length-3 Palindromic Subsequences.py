#
# @lc app=leetcode id=1930 lang=python3
#
# [1930] Unique Length-3 Palindromic Subsequences
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        ans = 0
        # 對所有字母，枚舉其第一次出現的下標和最後一次出現的下標
        for ch in ascii_lowercase:
            left, right = 0, n - 1
            while left < n and s[left] != ch: # 第一次出現的下標
                left += 1
            while right >= 0 and s[right] != ch: # 最後一次出現的下標
                right -= 1
            if right - left < 2: # 如果中間沒有別的字母，則不構成回文，或是該字母只出現一次或沒出現
                continue
            chars = set() # 統計中間出現的字母
            for k in range(left+1, right):
                chars.add(s[k])
            ans += len(chars)
        return ans

class Solution2:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        pre = [0] * 26
        suf = [0] * 26
        masks = [0] * 26
        for ch in s[1:]:
            suf[ord(ch) - ord('a')] += 1
        for i in range(1, n - 1):
            pre[ord(s[i - 1]) - ord('a')] += 1
            suf[ord(s[i]) - ord('a')] -= 1
            for j in range(26):
                if pre[j] > 0 and suf[j] > 0:
                    masks[ord(s[i]) - ord('a')] |= 1 << j 
        return sum(mask.bit_count() for mask in masks)

# Solution = Solution1
Solution = Solution2
# @lc code=end

