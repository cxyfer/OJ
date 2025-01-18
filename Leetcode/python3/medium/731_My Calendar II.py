#
# @lc app=leetcode id=731 lang=python3
# @lcpr version=30204
#
# [731] My Calendar II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class SegmentTree:
    def __init__(self):
        self.tree = defaultdict(lambda: [0, 0]) # (val, lazy)

    def update(self, o: int, left: int, right: int, l: int, r: int, v: int) -> None:
        if l <= left and right <= r:
            self.tree[o][0] += v
            self.tree[o][1] += v
            return
        self.pushdown(o)
        mid = (left + right) // 2
        if l <= mid:
            self.update(o * 2, left, mid, l, r, v)
        if r > mid:
            self.update(o * 2 + 1, mid + 1, right, l, r, v)
        self.pushup(o)

    def query(self, o: int, left: int, right: int, l: int, r: int) -> int:
        if l <= left and right <= r:
            return self.tree[o][0]
        self.pushdown(o)
        mid = (left + right) // 2
        ans = 0
        if l <= mid:
            ans = self.query(o * 2, left, mid, l, r)
        if r > mid:
            ans = max(ans, self.query(o * 2 + 1, mid + 1, right, l, r))
        return ans

    def pushdown(self, o: int) -> None:
        if self.tree[o][1] == 0:
            return
        self.tree[o * 2][0] += self.tree[o][1]
        self.tree[o * 2][1] += self.tree[o][1]
        self.tree[o * 2 + 1][0] += self.tree[o][1]
        self.tree[o * 2 + 1][1] += self.tree[o][1]
        self.tree[o][1] = 0

    def pushup(self, o: int) -> None:
        self.tree[o][0] = max(self.tree[o * 2][0], self.tree[o * 2 + 1][0])

class MyCalendarTwo:

    def __init__(self):
        self.st = SegmentTree()
        self.root = 1
        self.MAX = 10**9

    def book(self, start: int, end: int) -> bool:
        if self.st.query(self.root, 0, self.MAX, start, end-1) >= 2:
            return False
        self.st.update(self.root, 0, self.MAX, start, end-1, 1)
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
# @lc code=end


obj = MyCalendarTwo()
print(obj.book(10, 20)) # True
print(obj.book(50, 60)) # True
print(obj.book(10, 40)) # True
print(obj.book(5, 15)) # False
print(obj.book(5, 10)) # True
print(obj.book(25, 55)) # True

obj = MyCalendarTwo()
print(obj.book(24, 40)) # True
print(obj.book(43, 50)) # True
print(obj.book(27, 43)) # True
print(obj.book(5, 21)) # True
print(obj.book(30, 40)) # False
print(obj.book(14, 29)) # True
print(obj.book(3, 19)) # True
print(obj.book(3, 14)) # False
print(obj.book(25, 39)) # False