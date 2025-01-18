#
# @lc app=leetcode.cn id=2706 lang=python3
#
# [2706] 购买两块巧克力
#
from preImport import *
# @lc code=start
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1 = min2 = float('inf')
        for p in prices:
            if p < min1:
                min2 = min1
                min1 = p
            elif p < min2:
                min2 = p
        return money - (min1 + min2) if money >= min1 + min2 else money
# @lc code=end

