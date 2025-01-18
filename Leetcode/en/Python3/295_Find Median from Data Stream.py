# @algorithm @lc id=295 lang=python3 
from en.Python3.mod.preImport import *
# @title find-median-from-data-stream
class MedianFinder:
    def __init__(self):
        self.l = [] # max heap，保存比中位數小的數字，包含中位數
        self.r = [] # min heap，保存比中位數大的數字

    def addNum(self, num: int) -> None:
        if len(self.l) == len(self.r): # even
            if self.r and num > self.r[0]:
                heappush(self.l, -heappushpop(self.r, num))
            else:
                heappush(self.l, -num)
        else:
            if num < -self.l[0]:
                heappush(self.r, -heappushpop(self.l, -num))
            else:
                heappush(self.r, num)

    def findMedian(self) -> float:
        if len(self.l) == len(self.r):
            return (-self.l[0] + self.r[0]) / 2
        else:
            return -self.l[0]