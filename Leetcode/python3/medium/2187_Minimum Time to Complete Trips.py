#
# @lc app=leetcode id=2187 lang=python3
# @lcpr version=30204
#
# [2187] Minimum Time to Complete Trips
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def check(t):
            return sum(t // x for x in time) >= totalTrips

        left, right = 1, min(time) * totalTrips
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
# @lc code=end


#
# @lcpr case=start
# [1,2,3]\n5\n
# @lcpr case=end

# @lcpr case=start
# [2]\n1\n
# @lcpr case=end

#
