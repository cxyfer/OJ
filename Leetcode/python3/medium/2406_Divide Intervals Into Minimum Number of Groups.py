#
# @lc app=leetcode id=2406 lang=python3
# @lcpr version=30204
#
# [2406] Divide Intervals Into Minimum Number of Groups
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0])
        hp = []
        for left, right in intervals:
            if hp and left > hp[0]:
                heappop(hp)
            heappush(hp, right)
        return len(hp)
# @lc code=end



#
# @lcpr case=start
# [[5,10],[6,8],[1,5],[2,3],[1,10]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,3],[5,6],[8,10],[11,13]]\n
# @lcpr case=end

#

