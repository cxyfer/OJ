#
# @lc app=leetcode id=551 lang=python3
# @lcpr version=30204
#
# [551] Student Attendance Record I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        A, L = 0, 0
        for ch in s:
            if ch == 'L':
                L += 1
                if L >= 3:
                    return False
            else:
                if ch == 'A':
                    A += 1
                L = 0
        return A < 2
# @lc code=end



#
# @lcpr case=start
# "PPALLP"\n
# @lcpr case=end

# @lcpr case=start
# "PPALLL"\n
# @lcpr case=end

#

