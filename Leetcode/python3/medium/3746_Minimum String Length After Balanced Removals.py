#
# @lc app=leetcode id=3746 lang=python3
#
# [3746] Minimum String Length After Balanced Removals
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
let a = k, then b = n - k.
abs(a - b) = abs(2k - n)
"""
# @lc code=start
class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        # return abs(s.count('a') - s.count('b'))
        return abs(2 * s.count('a') - len(s))
# @lc code=end

