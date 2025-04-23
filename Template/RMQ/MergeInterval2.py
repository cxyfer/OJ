"""
    Merge Interval 2 - Using Node structure
    3525. Find X Value of Array II
"""
from typing import List

class Node:
    def __init__(self, prod: int, k: int):
        self.prod = prod
        self.cnt = [0] * k

class SegmentTree:
    def __init__(self, nums, k):
        n = len(nums)
        self.n = n
        self.k = k
        self.nums = [0] + nums  # 讓 index 從 1 開始
        self.tree = [None] * (1 << (n.bit_length() + 1))
        self.build(1, 1, n)

    def build(self, o, left, right):  # node, left, right
        if left == right:  # Leaf node initialization
            node = Node(self.nums[left], self.k)
            node.cnt[self.nums[left]] = 1
            self.tree[o] = node
            return
        mid = (left + right) // 2
        self.build(2*o, left, mid)  # left child
        self.build(2*o+1, mid + 1, right)  # right child
        self.tree[o] = self.merge(self.tree[2*o], self.tree[2*o+1])

    # 合併 [left, mid] 和 [mid+1, right] 兩部分的結果
    def merge(self, left, right):
        k = self.k
        prod = (left.prod * right.prod) % k
        node = Node(prod, k)
        for x in range(k):
            node.cnt[x] += left.cnt[x]
            node.cnt[(left.prod * x) % k] += right.cnt[x]
        return node

    def update(self, o, left, right, idx, val):
        if left == right:
            node = Node(val, self.k)
            node.cnt[val] = 1
            self.tree[o] = node
            return
        mid = (left + right) // 2
        if idx <= mid:
            self.update(2*o, left, mid, idx, val)
        else:
            self.update(2*o+1, mid + 1, right, idx, val)
        self.tree[o] = self.merge(self.tree[2*o], self.tree[2*o+1])

    def query(self, o, left, right, l, r):
        if left == l and r == right:
            return self.tree[o]
        mid = (left + right) // 2
        if r <= mid:  # 只需要查詢左半部分
            return self.query(2*o, left, mid, l, r)
        if mid < l:  # 只需要查詢右半部分
            return self.query(2*o+1, mid + 1, right, l, r)
        left_part = self.query(2*o, left, mid, l, mid)
        right_part = self.query(2*o+1, mid+1, right, mid+1, r)
        return self.merge(left_part, right_part)  # 合併左右兩部分