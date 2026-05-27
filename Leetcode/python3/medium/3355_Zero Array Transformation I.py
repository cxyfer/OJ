#
# @lc app=leetcode id=3355 lang=python3
#
# [3355] Zero Array Transformation I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        for l, r in queries:
            diff[l] += 1
            diff[r + 1] -= 1
        return all(s >= x for s, x in zip(accumulate(diff), nums))
# @lc code=end

