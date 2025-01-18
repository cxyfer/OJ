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
class SegNode:
    def __init__(self) -> None:
        self.ls = self.rs = None # left and right child
        self.val = self.lazy = 0 # value, lazy tag

class SegmentTree:
    def __init__(self):
        self.root = SegNode()
    
    # update the range [l, r] with value v
    @staticmethod
    def update(node: SegNode, left: int, right: int, l: int, r: int, v: int) -> None:
        if l <= left and right <= r:
            node.lazy += v
            node.val += v
            return
        SegmentTree.pushdown(node) # push down lazy tags
        mid = (left + right) // 2
        if l <= mid:
            SegmentTree.update(node.ls, left, mid, l, r, v)
        if r > mid:
            SegmentTree.update(node.rs, mid + 1, right, l, r, v)
        SegmentTree.pushup(node) # push up node value
 
    # query the range [l, r]
    @staticmethod
    def query(node: SegNode, left: int, right: int, l: int, r: int) -> int:
        if l <= left and right <= r:
            return node.val
        # Ensure all lazy tags have been pushed down
        SegmentTree.pushdown(node) 
        # Calculate answer: maximum value in this problem
        ans = 0
        mid = (left + right) // 2
        if l <= mid:
            ans = SegmentTree.query(node.ls, left, mid, l, r)
        if r > mid:
            ans = max(ans, SegmentTree.query(node.rs, mid + 1, right, l, r))
        return ans
    
    # push down lazy tags
    @staticmethod
    def pushdown(node: SegNode) -> None:
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
    @staticmethod
    def pushup(node: SegNode) -> None:
        # Update method: maximum value in this problem
        node.val = max(node.ls.val, node.rs.val)

class MyCalendarThree:

    def __init__(self):
        self.tree = SegmentTree()
        self.root = self.tree.root
        self.MAX = 10 ** 9

    def book(self, startTime: int, endTime: int) -> int:
        SegmentTree.update(self.root, 0, self.MAX, startTime, endTime - 1, 1)
        return self.root.val
    
# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)
# @lc code=end

obj = MyCalendarThree()
print(obj.book(10, 20)) # 1
print(obj.book(50, 60)) # 1
print(obj.book(10, 40)) # 2
print(obj.book(5, 15)) # 3
print(obj.book(5, 10)) # 3
print(obj.book(25, 55)) # 3
