#
# @lc app=leetcode.cn id=214 lang=python3
#
# [214] 最短回文串
#

# @lc code=start
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
        print(next)
        print(add)
        return s[n+2: n+2+add] + s[1:n+1] # 後半部分除去重疊後綴+前半部分
# @lc code=end
sol = Solution()
print(sol.shortestPalindrome("aacecaaa")) # "aaacecaaa"
print(sol.shortestPalindrome("abcd")) # "dcbabcd"
print(sol.shortestPalindrome("abacdecaba")) # "abacedcabacdecaba"
