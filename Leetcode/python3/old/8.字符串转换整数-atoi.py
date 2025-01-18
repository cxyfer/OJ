#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0
        positive = True
        ans = 0
        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return 0
        if s[i] == '-':
            positive = False
            i += 1
        elif s[i] == '+':
            i += 1
        while i < n and '0' <= s[i] <= '9':
            ans = ans * 10 + ord(s[i]) - ord('0')
            i += 1
            if positive and ans > 2**31-1:
                return 2**31-1
            elif not positive and ans > 2**31:
                return -2**31
        return ans if positive else -ans
# @lc code=end

