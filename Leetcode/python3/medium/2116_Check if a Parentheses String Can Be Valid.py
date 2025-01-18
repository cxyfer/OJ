#
# @lc app=leetcode id=2116 lang=python3
# @lcpr version=30204
#
# [2116] Check if a Parentheses String Can Be Valid
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n & 1:
            return False
        x = 0
        for i in range(n):
            if s[i] == '(' or locked[i] == '0':
                x += 1
            else:
                x -= 1
                if x < 0:
                    return False
        x = 0
        for i in range(n - 1, -1, -1):
            if s[i] == ')' or locked[i] == '0':
                x += 1
            else:
                x -= 1
                if x < 0:
                    return False
        return True
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

