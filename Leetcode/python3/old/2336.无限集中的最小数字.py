#
# @lc app=leetcode.cn id=2336 lang=python3
#
# [2336] 无限集中的最小数字
#
from en.Python3.mod.preImport import *
# @lc code=start
class SmallestInfiniteSet:

    def __init__(self):
        self.nums = [ i for i in range(1, 1001) ]
        heapify(self.nums)

    def popSmallest(self) -> int:
        return heappop(self.nums)

    def addBack(self, num: int) -> None:
        if num not in self.nums:
            heappush(self.nums, num)
            
# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
# @lc code=end

