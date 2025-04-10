from typing import *
from collections import defaultdict

"""
    Lazy Segment Tree
    - 使用 defaultdict 來保存節點

    Problem:
    - 731. My Calendar II
"""

class SegmentTree:
    def __init__(self):
        self.tree = defaultdict(lambda: [0, 0]) # (val, lazy)

    # update the range [l, r] with value v
    def update(self, o: int, left: int, right: int, l: int, r: int, v: int) -> None:
        if l <= left and right <= r:
            self.tree[o][0] += v
            self.tree[o][1] += v
            return
        self.pushdown(o) # push down lazy tags
        mid = (left + right) // 2
        if l <= mid:
            self.update(o * 2, left, mid, l, r, v)
        if r > mid:
            self.update(o * 2 + 1, mid + 1, right, l, r, v)
        self.pushup(o) # push up node value

    # query the range [l, r]
    def query(self, o: int, left: int, right: int, l: int, r: int) -> int:
        if l <= left and right <= r:
            return self.tree[o][0]
        # Ensure all lazy tags have been pushed down
        self.pushdown(o)
        # calculate answer: maximum value in this problem
        mid = (left + right) // 2
        ans = 0
        if l <= mid:
            ans = self.query(o * 2, left, mid, l, r)
        if r > mid:
            ans = max(ans, self.query(o * 2 + 1, mid + 1, right, l, r))
        return ans

    # push down lazy tags
    def pushdown(self, o: int) -> None:
        if self.tree[o][1] == 0:
            return
        self.tree[o * 2][0] += self.tree[o][1]
        self.tree[o * 2][1] += self.tree[o][1]
        self.tree[o * 2 + 1][0] += self.tree[o][1]
        self.tree[o * 2 + 1][1] += self.tree[o][1]
        self.tree[o][1] = 0 # clear current node's lazy tag

    # push up node value
    def pushup(self, o: int) -> None:
        self.tree[o][0] = max(self.tree[o * 2][0], self.tree[o * 2 + 1][0])