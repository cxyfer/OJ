#
# @lc app=leetcode id=1845 lang=python3
# @lcpr version=30204
#
# [1845] Seat Reservation Manager
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class SeatManager:

    def __init__(self, n: int):
        self.hp = list(range(1, n + 1))
        heapify(self.hp)

    def reserve(self) -> int:
        return heappop(self.hp)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.hp, seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
# @lc code=end



