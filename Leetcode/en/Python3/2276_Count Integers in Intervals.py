# @algorithm @lc id=2357 lang=python3 
# @title count-integers-in-intervals
from sortedcontainers import SortedList

class CountIntervals:
    def __init__(self):
        self.sl = SortedList(key=lambda x: x[1]) # 用右區間當索引key
        self.ans = 0 # 被染色的區間的長度和

    def add(self, left: int, right: int) -> None:
        i = self.sl.bisect_left((0, left)) # 找到第一個大於等於 left 的 key
        # print(left, right, i)
        # 遍歷所有被 [left,right] 覆蓋到的區間（部分覆蓋也算）
        while i < len(self.sl) and self.sl[i][0] <= right:
            l, r = self.sl[i]
            left = min(left, l) # 合併後的新區間，其左端點為所有被覆蓋的區間的左端點的最小值
            right = max(right, r) # 合併後的新區間，其右端點為所有被覆蓋的區間的右端點的最大值
            self.ans -= r - l + 1
            self.sl.pop(i)
        self.ans += right - left + 1
        self.sl.add((left, right))
        # print(self.sl)

    def count(self) -> int:
        return self.ans