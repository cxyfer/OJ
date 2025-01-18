#
# @lc app=leetcode.cn id=1503 lang=python3
#
# [1503] 所有蚂蚁掉下来前的最后一刻
#
from preImport import *
# @lc code=start
class Solution:
    """
        Similar to 2731. Movement of Robots
    """
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        # ans = 0
        # for pos in left:
        #     ans = max(ans, pos)
        # for pos in right:
        #     ans = max(ans, n-pos)
        # return ans
        return max(max(left + [0]), n-min(right + [n]))

# @lc code=end

