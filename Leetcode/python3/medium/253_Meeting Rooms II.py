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
        diff = defaultdict(int)
        for s, e in intervals:
            diff[s] += 1
            diff[e] -= 1
        ans = s = 0
        for _, d in sorted(diff.items()):
            s += d
            ans = max(ans, s)
        return ans
# @lc code=end

