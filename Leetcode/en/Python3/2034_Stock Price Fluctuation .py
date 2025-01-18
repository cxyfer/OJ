# @algorithm @lc id=2161 lang=python3 
# @title stock-price-fluctuation
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