# @algorithm @lc id=1955 lang=python3 
# @title seat-reservation-manager
import heapq

class SeatManager:
    def __init__(self, n: int):
        self.h = list(range(1, n+1))
        heapq.heapify(list(range(1, n+1)))

    def reserve(self) -> int:
        return heapq.heappop(self.h)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.h, seatNumber)