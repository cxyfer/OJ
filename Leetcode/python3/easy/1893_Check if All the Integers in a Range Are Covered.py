#
# @lc app=leetcode id=1893 lang=python3
#
# [1893] Check if All the Integers in a Range Are Covered
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = [0] * (right + 2)
        for l, r in ranges:
            if l > right or r < left:
                continue
            diff[max(l, left)] += 1
            diff[min(r, right) + 1] -= 1

        s = 0
        for i in range(left, right + 1):
            s += diff[i]
            if s <= 0:
                return False
        return True
# @lc code=end

