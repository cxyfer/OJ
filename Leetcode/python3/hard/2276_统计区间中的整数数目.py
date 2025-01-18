#
# @lc app=leetcode.cn id=2276 lang=python3
#
# [2276] 统计区间中的整数数目
#
# @lc code=start
from sortedcontainers import SortedList

class CountIntervals1:
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

class CountIntervals2:
    __slots__ = 'left', 'right', 'l', 'r', 'cnt'

    def __init__(self, l=1, r=10 ** 9):
        self.left = self.right = None # 左右子樹
        self.l, self.r, self.cnt = l, r, 0 # 區間左右端點，被染色的區間的長度和

    def add(self, L: int, R: int) -> None:
        if self.cnt == self.r - self.l + 1: return # self 已被完全染色，無需操作
        if L <= self.l and self.r <= R: # self 已被 [L,R] 完全覆蓋，直接染色
            self.cnt = self.r - self.l + 1
            return
        mid = (self.l + self.r) // 2 # self 的中點
        if self.left is None: self.left = CountIntervals(self.l, mid) # 動態開點
        if self.right is None: self.right = CountIntervals(mid + 1, self.r) # 動態開點
        if L <= mid: self.left.add(L, R) # 將 [L,R] 覆蓋到 self 的左子樹
        if mid < R: self.right.add(L, R) # 將 [L,R] 覆蓋到 self 的右子樹
        self.cnt = self.left.cnt + self.right.cnt # 更新 self 的被染色的區間的長度和

    def count(self) -> int:
        return self.cnt

class CountIntervals(CountIntervals2):
    pass

# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()
# @lc code=end
obj = CountIntervals()
obj.add(2,3)
obj.add(7,10)
print(obj.count()) # 6
obj.add(5,8)
print(obj.count()) # 8

obj = CountIntervals()
print(obj.count()) # 0
obj.add(8,43)
obj.add(13,16)
obj.add(26,33)
obj.add(28,36)
obj.add(29,37)
print(obj.count()) # 36
obj.add(34,46)
obj.add(10,23)