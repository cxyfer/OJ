#
# @lc app=leetcode id=732 lang=python3
# @lcpr version=30204
#
# [732] My Calendar III
#


# @lcpr-template-start
from preImport import *

# @lcpr-template-end
# @lc code=start
from sortedcontainers import SortedDict


class MyCalendarThree1:
    def __init__(self):
        self.diff = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.diff[start] = self.diff.get(start, 0) + 1
        self.diff[end] = self.diff.get(end, 0) - 1

        ans = s = 0
        for v in self.diff.values():
            s += v
            ans = max(ans, s)
        return ans


class SegNode:
    def __init__(self) -> None:
        self.ls = self.rs = None  # left and right child
        self.val = self.lazy = 0  # value, lazy tag


class SegmentTree:
    def __init__(self):
        self.root = SegNode()

    # update the range [l, r] with value v
    def update(self, node: SegNode, left: int, right: int, l: int, r: int, v: int) -> None:  # fmt: skip
        if l <= left and right <= r:
            node.lazy += v
            node.val += v
            return
        self.pushdown(node)  # push down lazy tags
        mid = (left + right) // 2
        if l <= mid:
            self.update(node.ls, left, mid, l, r, v)
        if r > mid:
            self.update(node.rs, mid + 1, right, l, r, v)
        self.pushup(node)  # push up node value

    # query the range [l, r]
    def query(self, node: SegNode, left: int, right: int, l: int, r: int) -> int:  # fmt: skip
        if l <= left and right <= r:
            return node.val
        self.pushdown(node)
        ans = 0
        mid = (left + right) // 2
        if l <= mid:
            ans = self.query(node.ls, left, mid, l, r)
        if r > mid:
            ans = max(ans, self.query(node.rs, mid + 1, right, l, r))
        return ans

    # push down lazy tags
    def pushdown(self, node: SegNode) -> None:
        if node.ls is None:
            node.ls = SegNode()
        if node.rs is None:
            node.rs = SegNode()
        if node.lazy:
            node.ls.lazy += node.lazy
            node.rs.lazy += node.lazy
            node.ls.val += node.lazy
            node.rs.val += node.lazy
            node.lazy = 0

    # push up node value
    def pushup(self, node: SegNode) -> None:
        node.val = max(node.ls.val, node.rs.val)


class MyCalendarThree2:
    def __init__(self):
        self.seg = SegmentTree()
        self.root = self.seg.root
        self.MAX = int(1e9)

    def book(self, startTime: int, endTime: int) -> int:
        self.seg.update(self.root, 0, self.MAX, startTime, endTime - 1, 1)
        return self.root.val


# MyCalendarThree = MyCalendarThree1
MyCalendarThree = MyCalendarThree2

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)
# @lc code=end

obj = MyCalendarThree()
print(obj.book(10, 20))  # 1
print(obj.book(50, 60))  # 1
print(obj.book(10, 40))  # 2
print(obj.book(5, 15))  # 3
print(obj.book(5, 10))  # 3
print(obj.book(25, 55))  # 3
