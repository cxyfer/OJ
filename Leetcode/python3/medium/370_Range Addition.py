#
# @lc app=leetcode id=370 lang=python3
#
# [370] Range Addition
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def getModifiedArray(self, n: int, updates: List[List[int]]) -> List[int]:
        diff = [0] * n
        for l, r, v in updates:
            diff[l] += v
            if r + 1 < n:
                diff[r + 1] -= v
        return list(accumulate(diff))
# @lc code=end

