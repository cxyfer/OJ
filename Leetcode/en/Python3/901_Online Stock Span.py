# @algorithm @lc id=937 lang=python3 
# @title online-stock-span
from collections import deque
class StockSpanner1:
    """
        Monotonic stack
        在Stack存放的是index，但對應的element是遞減的
    """
    def __init__(self):
        self.prices = [float("inf")]
        self.st = deque([0])
        self.idx = 0

    def next(self, price: int) -> int:
        self.prices.append(price)
        self.idx += 1
        while self.st and price >= self.prices[self.st[-1]]:
            self.st.pop()
        self.st.append(self.idx)
        return self.st[-1] - self.st[-2]
class StockSpanner2:
    """
        也可以直接在Stack中存(idx, price)
    """
    def __init__(self):
        self.st = [(-1, float("inf"))] # (index, price)
        self.idx = -1

    def next(self, price: int) -> int:
        self.idx += 1
        while self.st and price >= self.st[-1][1]:
            self.st.pop()
        self.st.append((self.idx, price))
        return self.st[-1][0] - self.st[-2][0]
class StockSpanner(StockSpanner2):
    ...