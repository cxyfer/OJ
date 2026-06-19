#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(accumulate(gain, initial=0))
# @lc code=end

