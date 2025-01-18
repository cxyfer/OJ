0#
# @lc app=leetcode.cn id=2034 lang=python3
#
# [2034] 股票价格波动
#
from preImport import *

# @lc code=start
from sortedcontainers import SortedList

class StockPrice:
    def __init__(self):
        self.time = {} # timestamp: price
        self.prices = SortedList()
        self.cur = 0 # current timestamp

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.time:
            self.prices.remove(self.time[timestamp])
        self.time[timestamp] = price
        self.prices.add(price)
        self.cur = max(self.cur, timestamp) # update current timestamp

    def current(self) -> int:
        return self.time[self.cur]

    def maximum(self) -> int:
        return self.prices[-1]

    def minimum(self) -> int:
        return self.prices[0]



# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
# @lc code=end

