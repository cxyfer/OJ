#
# @lc app=leetcode id=3169 lang=python3
# @lcpr version=30203
#
# [3169] Count Days Without Meetings
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Similar to 56. Merge Intervals
    """
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        res = [meetings[0]]
        for x, y in meetings:
            if x > res[-1][1]:
                res.append([x, y])
            else:
                res[-1][1] = max(res[-1][1], y)
        ans = days
        for x, y in res:
            ans -= y - x + 1
        return ans
# @lc code=end



#
# @lcpr case=start
# 10\n[[5,7],[1,3],[9,10]]\n
# @lcpr case=end

# @lcpr case=start
# 5\n[[2,4],[1,3]]\n
# @lcpr case=end

# @lcpr case=start
# 6\n[[1,6]]\n
# @lcpr case=end

#

