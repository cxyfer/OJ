#
# @lc app=leetcode id=2483 lang=python3
#
# [2483] Minimum Penalty for a Shop
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        pre = 0
        suf = sum(c == 'Y' for c in customers)
        ans, cost = 0, suf
        for i, c in enumerate(customers, 1):
            if c == 'N':
                pre += 1
            else:
                suf -= 1
            if pre + suf < cost:
                ans = i
                cost = pre + suf
        return ans
# @lc code=end

