#
# @lc app=leetcode.cn id=1845 lang=python3
#
# [1845] 座位预约管理系统
#
from preImport import *
# @lc code=start
class SeatManager:
    def __init__(self, n: int):
        self.h = list(range(1, n+1))
        heapq.heapify(list(range(1, n+1)))

    def reserve(self) -> int:
        return heapq.heappop(self.h)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.h, seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
# @lc code=end

