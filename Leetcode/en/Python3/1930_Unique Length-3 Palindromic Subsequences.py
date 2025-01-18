# @algorithm @lc id=2059 lang=python3 
# @title unique-length-3-palindromic-subsequences


from en.Python3.mod.preImport import *
from string import ascii_lowercase
# @test("aabca")=3
# @test("adc")=0
# @test("bbcbaba")=4
class Solution:
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