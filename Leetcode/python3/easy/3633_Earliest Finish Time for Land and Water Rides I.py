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
        intervals1 = [(st, d) for st, d in zip(landStartTime, landDuration)]
        intervals2 = [(st, d) for st, d in zip(waterStartTime, waterDuration)]

        def calc(intervals1, intervals2):
            min_ed = min(st + d for st, d in intervals1)
            return min(max(min_ed, st) + d for st, d in intervals2)

        return min(calc(intervals1, intervals2), calc(intervals2, intervals1))
# @lc code=end

