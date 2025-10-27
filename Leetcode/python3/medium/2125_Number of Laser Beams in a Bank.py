#
# @lc app=leetcode id=2125 lang=python3
#
# [2125] Number of Laser Beams in a Bank
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        nums = [v for row in bank if (v := row.count('1')) > 0]
        return sum(x * y for x, y in pairwise(nums))
# @lc code=end

