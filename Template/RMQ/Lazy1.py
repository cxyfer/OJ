from typing import *

"""
    Lazy Segment Tree
    - 動態開點，只有當需要用到子節點時，才會創建子節點

    Problem:
    - 731. My Calendar II
"""

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