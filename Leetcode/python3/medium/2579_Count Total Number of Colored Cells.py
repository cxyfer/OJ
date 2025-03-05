#
# @lc app=leetcode.cn id=2579 lang=python3
# @lcpr version=30204
#
# [2579] 统计染色格子数
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    2 * (1 + 3 + ... + (2n - 1)) - (2n - 1)
= 2 * ((1 + (2n - 1)) * n / 2) - (2n - 1)
= 2 * (n^2) - (2n - 1)
"""
class Solution:
    def coloredCells(self, n: int) -> int:
        return 2 * n * n - 2 * n + 1
# @lc code=end



#
# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

#

