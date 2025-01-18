#
# @lc app=leetcode id=647 lang=python3
# @lcpr version=30204
#
# [647] Palindromic Substrings
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    1. Dynamic Programming
       dp[i][j] = True if s[i:j+1] is a palindrome
    2. Manacher Algorithm
"""
class Solution1:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = 0
        for i in range(n): # 長度為 1 的palindrome substring
            dp[i][i] = True
            ans += 1
        for i in range(n-1): # 長度為 2 的palindrome substring
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans += 1
        for ln in range(3, n+1): # 長度 >= 3 的palindrome substring
            for i in range(n-ln+1): # 枚舉起始位置
                j = i + ln - 1 # 終止位置
                if s[i] == s[j] and dp[i+1][j-1]: # 如果 s[i] == s[j] 且 s[i+1:j-1] 是 palindrome
                    dp[i][j] = True
                    ans += 1
        return ans

class Solution2:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        t = '#'.join("^" + s + "$")
        halfLen = [0] * (len(t) - 2)
        halfLen[1] = 1
        boxM = boxR = 0
        for i in range(2, len(halfLen)):
            hl = 1
            if i < boxR:
                hl = min(halfLen[boxM * 2 - i], boxR - i)
            while t[i - hl] == t[i + hl]:
                hl += 1
                boxM, boxR = i, i + hl
            halfLen[i] = hl
            if i % 2 == 0: # 偶數位置對應真正的字母，回文子字串長度為奇數
                # print(i, hl, t[i-hl+1:i+hl])
                ans += hl // 2
            else: # 奇數位置對應 #，回文子字串長度為偶數
                # print(i, hl, t[i-hl+1:i+hl])
                ans += (hl - 1) // 2 # 減去一個 #
        return ans
    
# class Solution(Solution1):
class Solution(Solution2):
    pass
# @lc code=end

sol = Solution()
# print(sol.countSubstrings("abc")) # 3
print(sol.countSubstrings("aaa")) # 6

#
# @lcpr case=start
# "abc"\n
# @lcpr case=end

# @lcpr case=start
# "aaa"\n
# @lcpr case=end

#

