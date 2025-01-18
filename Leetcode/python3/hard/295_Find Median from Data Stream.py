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
        self.l = []
        # min heap，保存 > median 的數字
        self.r = []

    def addNum(self, num: int) -> None:
        # 當前數量為偶數，加入到左邊
        if len(self.l) == len(self.r):
            # 如果新加入的數字比右邊的最小值還要大，則先加入到右邊，再將右邊的最小值加入到左邊
            if self.r and num > self.r[0]:
                heappush(self.l, -heappushpop(self.r, num))
            else:
                heappush(self.l, -num)
        # 當前數量為奇數，加入到右邊
        else:
            # 如果新加入的數字比左邊的最大值還要小，則先加入到左邊，再將左邊的最大值加入到右邊
            if num < -self.l[0]:
                heappush(self.r, -heappushpop(self.l, -num))
            else:
                heappush(self.r, num)

    def findMedian(self) -> float:
        return (-self.l[0] + self.r[0]) / 2 if len(self.l) == len(self.r) else -self.l[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
