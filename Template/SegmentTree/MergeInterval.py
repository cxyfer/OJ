
from typing import List

"""
    3187. Peaks in Array
    3161. Block Placement Queries
"""

class SegmentTree:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.n = n
        self.nums = [0] + nums # 讓 index 從 1 開始
        # self.tree = [0 for _ in range(4 * n)]
        self.tree = [0] * (1 << (n.bit_length() + 1))
        self.build(1, 1, n)
 
    def build(self, o, left, right): # node, left, right
        if left == right: # Leaf node initialization
            self.tree[o] = 0
            return
        mid = (left + right) // 2
        self.build(2*o, left, mid) # left child
        self.build(2*o+1, mid + 1, right) # right child
        self.tree[o] = self.merge(self.tree[2*o], self.tree[2*o+1], left, mid, right)

    # 合併 [left, mid] 和 [mid+1, right] 兩部分的結果
    def merge(self, left_part, right_part, left, mid, right):
        res = left_part + right_part
        if mid - 1 >= left and self.nums[mid-1] < self.nums[mid] > self.nums[mid+1] \
            or mid + 2 <= right and self.nums[mid] < self.nums[mid+1] > self.nums[mid+2]:
            res += 1
        return res

    def update(self, o, left, right, idx, val):
        if left == right:
            self.nums[idx] = val
            self.tree[o] = 0
            return
        mid = (left + right) // 2
        if idx <= mid:
            self.update(2*o, left, mid, idx, val)
        else:
            self.update(2*o+1, mid + 1, right, idx, val)
        self.tree[o] = self.merge(self.tree[2*o], self.tree[2*o+1], left, mid, right)
 
    def query(self, o, left, right, l, r):
        if left == l and r == right:
            return self.tree[o]
        mid = (left + right) // 2
        if r <= mid: # 只需要查詢左半部分
            return self.query(2*o, left, mid, l, r)
        if mid < l: # 只需要查詢右半部分
            return self.query(2*o+1, mid + 1, right, l, r)
        left_part = self.query(2*o, left, mid, l, mid)
        right_part = self.query(2*o+1, mid+1, right, mid+1, r)
        return self.merge(left_part, right_part, l, mid, r) # 合併左右兩部分