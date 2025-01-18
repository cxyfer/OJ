#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return self.bruteForce(haystack, needle)
        return self.kmp(haystack, needle)
    """
        1. Brute Force
    """
    def bruteForce(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if not needle:
            return 0
        for i in range(m - n + 1): # 枚舉起始點
            if haystack[i:i+n] == needle:
                return i
        return -1
    """
        2. KMP
    """
    def kmp(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        def getNext(needle):
            next = [-1] * len(needle)
            i = 0
            j = -1
            while i < len(needle) - 1:
                if j == -1 or needle[i] == needle[j]:
                    i += 1
                    j += 1
                    next[i] = j
                else:
                    j = next[j]
            return next
        
        next = getNext(needle)
        i = j = 0
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == len(needle):
            return i - j
        else:
            return -1
# @lc code=end

