#
# @lc app=leetcode id=3633 lang=python3
#
# [3633] Earliest Finish Time for Land and Water Rides I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def helper(interval1: List[Tuple[int, int]], interval2: List[Tuple[int, int]]) -> int:
            res = min(st + d for st, d in interval1)
            return min(max(st, res) + d for st, d in interval2)
        return min(helper(zip(landStartTime, landDuration), zip(waterStartTime, waterDuration)), helper(zip(waterStartTime, waterDuration), zip(landStartTime, landDuration)))
# @lc code=end

