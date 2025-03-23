#
# @lc app=leetcode id=2116 lang=python3
# @lcpr version=30204
#
# [2116] Check if a Parentheses String Can Be Valid
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. Greedy (Two-pass)
    - 確保從左到右的能變成 '(' 的數量大於 ')' 的數量，反之同理
2. Greedy (One-pass)
    - Similar to 678. Valid Parenthesis String
    - 維護可能的 cnt 取值範圍
"""
# @lc code=start
class Solution1:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n & 1:
            return False
        cnt = 0
        for ch, lk in zip(s, locked):
            if ch == '(' or lk == '0':
                cnt += 1
            else:
                cnt -= 1
                if cnt < 0:
                    return False
        cnt = 0
        for ch, lk in zip(s[::-1], locked[::-1]):
            if ch == ')' or lk == '0':
                cnt += 1
            else:
                cnt -= 1
                if cnt < 0:
                    return False
        return True

class Solution2:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) & 1:
            return False
        mn = mx = 0
        for ch, lk in zip(s, locked):
            if lk == '1':
                if ch == '(':
                    mn += 1
                    mx += 1
                elif ch == ')':
                    mn = max(0, mn - 1)
                    mx -= 1
                    if mx < 0:
                        return False
            else:
                mn = max(0, mn - 1)
                mx += 1
        return mn == 0

# Solution = Solution1
Solution = Solution2
# @lc code=end



#
# @lcpr case=start
# "))()))"\n"010100"\n
# @lcpr case=end

# @lcpr case=start
# "()()"\n"0000"\n
# @lcpr case=end

# @lcpr case=start
# ")"\n"0"\n
# @lcpr case=end

#

