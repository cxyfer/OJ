# @algorithm @lc id=2413 lang=python3 
from en.Python3.mod.preImport import *
# @title smallest-number-in-infinite-set
class SmallestInfiniteSet:

    def __init__(self):
        self.nums = [ i for i in range(1, 1001) ]
        heapify(self.nums)

    def popSmallest(self) -> int:
        return heappop(self.nums)

    def addBack(self, num: int) -> None:
        if num not in self.nums:
            heappush(self.nums, num)
            