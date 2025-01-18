#
# @lc app=leetcode id=3340 lang=python3
# @lcpr version=30204
#
# [3340] Check Balanced String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def isBalanced(self, num: str) -> bool:
        # return sum((ord(d) - ord('0')) * (-1 if idx & 1 else 1) for idx, d in enumerate(num)) == 0
        s1 = s2 = 0
        for idx, d in enumerate(num):
            if idx % 2 == 0:
                s1 += ord(d) - ord('0')
            else:
                s2 += ord(d) - ord('0')
        return s1 == s2
# @lc code=end



#
# @lcpr case=start
# "1234"\n
# @lcpr case=end

# @lcpr case=start
# "24123"\n
# @lcpr case=end

#

