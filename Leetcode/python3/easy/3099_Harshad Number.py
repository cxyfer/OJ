#
# @lc app=leetcode id=3099 lang=python3
# @lcpr version=30204
#
# [3099] Harshad Number
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s, tmp = 0, x
        while tmp:
            tmp, r = divmod(tmp, 10)
            s += r
        return s if x % s == 0 else -1
# @lc code=end



#
# @lcpr case=start
# 18\n
# @lcpr case=end

# @lcpr case=start
# 23\n
# @lcpr case=end

#

