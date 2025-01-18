#
# @lc app=leetcode id=5 lang=python3
# @lcpr version=30204
#
# [5] Longest Palindromic Substring
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    1. Dynamic Programming: O(n^2)
       dp[i][j] 表示 s[i..j] 是否為回文串
    2. Manacher: O(n)
"""
class Solution1:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1: return s
        dp = [[False] * n for _ in range(n)]
        for i in range(n): # 初始化：所有長度為1的子串都是回文串
            dp[i][i] = True
        ans = 1 # 最長回文子串長度
        st = 0 # 最長回文子串起點
        for ln in range(2, n+1): # 枚舉子字串的長度
            for i in range(n-ln+1): # 枚舉子字串的起點
                j = i + ln - 1 # 子字串的終點
                if s[i] == s[j] and (ln == 2 or dp[i+1][j-1]): # 頭尾相等且去掉頭尾之後還是回文串
                    dp[i][j] = True
                    if ln > ans: # 更新最長回文子串長度和起點
                        ans = ln
                        st = i
        return s[st:st+ans]
    
class Manacher:
    def __init__(self, s) -> None:
        self.s = s
        if isinstance(s, str):
            self.t = '#'.join("^" + s + "$")
        elif isinstance(s, list):
            self.t = '#'.join(['^'] + s + ['$'])
        else:
            raise ValueError("s must be a string or a list")
        
        self.halfLen = [0] * (len(self.t) - 2)
        self.halfLen[1] = 1
        boxM = boxR = 0
        self.max_i = 0 # 最長回文子字串的中心位置
        for i in range(2, len(self.halfLen)):
            hl = 1
            if i < boxR:
                hl = min(self.halfLen[boxM * 2 - i], boxR - i)
            while self.t[i - hl] == self.t[i + hl]:
                hl += 1
                boxM, boxR = i, i + hl
            self.halfLen[i] = hl
            if hl > self.halfLen[self.max_i]:
                self.max_i = i

    # 判斷 s[l:r] 是否為回文字串
    def isPalindrome(self, l: int, r: int) -> bool:
        return self.halfLen[l + r + 1] > r - l
    
    # 獲取最長回文子字串的長度
    def getMaxPalindromeLength(self) -> int:
        return self.halfLen[self.max_i] - 1
    
    # 獲取最長回文子字串
    def getMaxPalindrome(self) -> str:
        hl = self.halfLen[self.max_i]
        return self.s[(self.max_i - hl) // 2:(self.max_i + hl) // 2 - 1]
    
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        manacher = Manacher(s)
        return manacher.getMaxPalindrome()

# class Solution(Solution1):
class Solution(Solution2):
    pass
# @lc code=end

sol = Solution()
print(sol.longestPalindrome("babad"))

#
# @lcpr case=start
# "babad"\n
# @lcpr case=end

# @lcpr case=start
# "cbbd"\n
# @lcpr case=end

#

