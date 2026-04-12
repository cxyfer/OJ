#
# @lc app=leetcode id=1109 lang=python3
#
# [1109] Corporate Flight Bookings
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * n
        for l, r, v in bookings:
            diff[l - 1] += v
            if r < n:
                diff[r] -= v
        return list(accumulate(diff))
# @lc code=end
sol = Solution()
print(sol.corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]], 5))  # [10,55,45,25,25]