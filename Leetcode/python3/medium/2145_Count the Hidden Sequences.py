#
# @lc app=leetcode id=2145 lang=python3
#
# [2145] Count the Hidden Sequences
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        s = list(accumulate(differences, initial=lower))
        return max(upper - (max(s) + lower - min(s)) + 1, 0)
# @lc code=end

