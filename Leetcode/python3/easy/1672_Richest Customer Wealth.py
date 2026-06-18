#
# @lc app=leetcode id=1672 lang=python3
#
# [1672] Richest Customer Wealth
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(row) for row in accounts)
# @lc code=end

