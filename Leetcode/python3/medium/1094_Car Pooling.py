#
# @lc app=leetcode id=1094 lang=python3
#
# [1094] Car Pooling
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_r = max(r for _, _, r in trips)
        diff = [0] * (max_r + 1)
        for val, l, r in trips:
            diff[l] += val
            diff[r] -= val
        return all(s <= capacity for s in accumulate(diff))
# @lc code=end