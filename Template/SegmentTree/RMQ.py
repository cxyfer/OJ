from typing import *

"""
    Range Minimum Queries (RMQ)

    這種寫法的 Segment Tree 以下兩題使用 Python 會超時
    - CSES-1647 Static Range Minimum Queries
    - CSES-1649 Dynamic Range Minimum Queries
"""

class SegmentTree:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.nums = [0] + nums # 讓 index 從 1 開始
        # self.tree = [0 for _ in range(4 * n)]
        self.tree = [0 for _ in range(1 << (n.bit_length() + 1))]
        self.build(1, 1, n)
 
    def build(self, o, left, right): # node, left, right
        if left == right: # Leaf node initialization
            self.tree[o] = self.nums[left]
            return
        mid = (left + right) // 2
        self.build(2*o, left, mid) # left child
        self.build(2*o+1, mid + 1, right) # right child
        self.tree[o] = self.merge(2*o, 2*o+1)
 
    def merge(self, left_child, right_child):
        return min(self.tree[left_child], self.tree[right_child])
 
    def update(self, o, left, right, idx, val):
        if left == right:
            self.tree[o] = val
            return
        mid = (left + right) // 2
        if idx <= mid:
            self.update(2*o, left, mid, idx, val)
        else:
            self.update(2*o+1, mid + 1, right, idx, val)
        self.tree[o] = self.merge(2*o, 2*o+1)
 
    def query(self, o, left, right, l, r):
        if l <= left and right <= r:
            return self.tree[o]
        mid = (left + right) // 2
        ans = float('inf')
        if l <= mid:
            ans = min(ans, self.query(2*o, left, mid, l, r))
        if r > mid:
            ans = min(ans, self.query(2*o+1, mid + 1, right, l, r))
        return ans
 