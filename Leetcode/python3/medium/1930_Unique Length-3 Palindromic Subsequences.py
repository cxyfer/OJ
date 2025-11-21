#
# @lc app=leetcode id=1930 lang=python3
#
# [1930] Unique Length-3 Palindromic Subsequences
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
# 1. 枚舉

目標是找出所有長度為 3 的回文子序列
由於一定是 ABA 的形式，故我們可以枚舉 A，然後找出有多少種不同的 B

# 2. 前後綴分解
"""
# @lc code=start
class Solution1:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        ans = 0
        for ch in ascii_lowercase:  # 枚舉兩側對稱的字母
            left, right = 0, n - 1
            while left < n and s[left] != ch:  # 第一次出現的下標
                left += 1
            while right >= 0 and s[right] != ch:  # 最後一次出現的下標
                right -= 1
            if right - left < 2:  # 如果中間沒有別的字母，或是該字母沒有出現過兩次，則無法構成回文
                continue
            ans += len(set(s[left+1:right])) # 統計中間出現的字母
        return ans

class Solution2:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        pre = [0] * 26
        suf = [0] * 26
        masks = [0] * 26  # 以 ch 為中心，左側和右側的字母出現情況
        for ch in s[1:]:
            suf[ord(ch) - ord('a')] += 1
        for i in range(1, n - 1):  # 枚舉中心字母
            pre[ord(s[i - 1]) - ord('a')] += 1
            suf[ord(s[i]) - ord('a')] -= 1
            for j in range(26):
                if pre[j] > 0 and suf[j] > 0:
                    masks[ord(s[i]) - ord('a')] |= 1 << j 
        return sum(mask.bit_count() for mask in masks)

# Solution = Solution1
Solution = Solution2
# @lc code=end

