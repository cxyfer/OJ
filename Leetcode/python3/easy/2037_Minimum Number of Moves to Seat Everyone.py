#
# @lc app=leetcode id=2037 lang=python3
# @lcpr version=30203
#
# [2037] Minimum Number of Moves to Seat Everyone
#

# @lcpr-template-start
from preImport import *

# @lcpr-template-end
# @lc code=start
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        return sum(abs(x - y) for x, y in zip(seats, students))
# @lc code=end

sol = Solution()
print(sol.minMovesToSeat([3, 1, 5], [2, 7, 4])) # 4
print(sol.minMovesToSeat([4, 1, 5, 9], [1, 3, 2, 6])) # 7
print(sol.minMovesToSeat([2, 2, 6, 6], [1, 3, 2, 6])) # 4

#
# @lcpr case=start
# [3,1,5]\n[2,7,4]\n
# @lcpr case=end

# @lcpr case=start
# [4,1,5,9]\n[1,3,2,6]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,6,6]\n[1,3,2,6]\n
# @lcpr case=end

#
