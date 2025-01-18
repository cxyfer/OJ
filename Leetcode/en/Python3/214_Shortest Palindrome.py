# @algorithm @lc id=214 lang=python3 
# @title shortest-palindrome

from en.Python3.mod.preImport import *
# @test("aacecaaa")="aaacecaaa"
# @test("abcd")="dcbabcd"
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        s = ' ' + s + '#' + s[::-1] # 讓下標從1開始
        m = 2 * n + 1 # 實際長度
        # KMP
        next = [0] * (m + 1) # next function in KMP
        k = 0
        for i in range(2, m + 1): # [2, 2*n+1]
            while k > 0 and s[k + 1] != s[i]:
                k = next[k]
            if s[k + 1] == s[i]:
                k += 1
            next[i] = k
        # Answer
        add = n - next[2 * n + 1] # 需要添加的字元數
        return s[n+2: n+2+add] + s[1:n+1] # 後半部分除去重疊後綴+前半部分