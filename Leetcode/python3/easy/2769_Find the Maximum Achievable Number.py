#
# @lc app=leetcode id=2769 lang=python3
# @lcpr version=30202
#
# [2769] Find the Maximum Achievable Number
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        x - t = num + t
        x = num + 2t
    """
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + (t << 1)
# @lc code=end



#
# @lcpr case=start
# 4\n1\n
# @lcpr case=end

# @lcpr case=start
# 3\n2\n
# @lcpr case=end

#

