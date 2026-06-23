#
# @lc app=leetcode id=295 lang=python3
# @lcpr version=30201
#
# [295] Find Median from Data Stream
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class MedianFinder:
    def __init__(self):
        # max heap，保存 <= median 的數字
        self.L = []
        # min heap，保存 > median 的數字
        self.R = []

    def addNum(self, num: int) -> None:
        # 當前數量為偶數，加入到左邊
        if len(self.L) == len(self.R):
            # 如果新加入的數字比右邊的最小值還要大，則先加入到右邊，再將右邊的最小值加入到左邊
            if self.R and num > self.R[0]:
                heappush_max(self.L, heappushpop(self.R, num))
            else:
                heappush_max(self.L, num)
        # 當前數量為奇數，加入到右邊
        else:
            # 如果新加入的數字比左邊的最大值還要小，則先加入到左邊，再將左邊的最大值加入到右邊
            if num < self.L[0]:
                heappush(self.R, heappushpop_max(self.L, num))
            else:
                heappush(self.R, num)

    def findMedian(self) -> float:
        return (self.L[0] + self.R[0]) / 2 if len(self.L) == len(self.R) else self.L[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
