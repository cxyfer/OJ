#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        diff = [0] * (int(1e6 + 5))
        for s, e in intervals:
            diff[s] += 1
            diff[e] -= 1
        ans = s = 0
        for d in diff:
            s += d
            ans = max(ans, s)
        return ans
# @lc code=end

