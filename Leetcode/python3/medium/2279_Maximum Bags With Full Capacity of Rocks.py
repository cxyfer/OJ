#
# @lc app=leetcode id=2279 lang=python3
#
# [2279] Maximum Bags With Full Capacity of Rocks
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        diffs = [c - r for c, r in zip(capacity, rocks)]
        diffs.sort()
        for i, d in enumerate(diffs):
            if additionalRocks < d:
                return i
            additionalRocks -= d
        return n
# @lc code=end

