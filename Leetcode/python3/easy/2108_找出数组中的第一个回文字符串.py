#
# @lc app=leetcode.cn id=2108 lang=python3
#
# [2108] 找出数组中的第一个回文字符串
#
from preImport import *
# @lc code=start
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(s):
            n = len(s)
            for i in range(n//2):
                if s[i] != s[n-1-i]:
                    return False
            return True
        for word in words:
            if isPalindrome(word):
                return word
        return ""
# @lc code=end

