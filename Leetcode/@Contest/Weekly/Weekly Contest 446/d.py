import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Node:
    def __init__(self, prod: int = None, cnt: List[int] = None):
        self.prod = prod
        self.cnt = cnt

class SegmentTree:
    def __init__(self, nums, k):
        n = len(nums)
        self.n = n
        self.k = k
        self.nums = [0] + nums # 讓 index 從 1 開始
        self.tree = [0] * (1 << (n.bit_length() + 1))
        self.build(1, 1, n)

    def build(self, o, left, right): # node, left, right
        if left == right: # Leaf node initialization
            prod = self.nums[left] % self.k
            cnt = [0] * self.k
            cnt[prod] = 1
            self.tree[o] = Node(prod, cnt)
            return
        mid = (left + right) // 2
        self.build(2*o, left, mid) # left child
        self.build(2*o+1, mid + 1, right) # right child
        self.tree[o] = self.merge(self.tree[2*o], self.tree[2*o+1], left, mid, right)

    # 合併 [left, mid] 和 [mid+1, right] 兩部分的結果
    def merge(self, left_part, right_part, left, mid, right):
        pl, pr = left_part.prod, right_part.prod
        cntl, cntr = left_part.cnt, right_part.cnt

        k = self.k
        prod = (pl * pr) % k
        cnt = [0] * k
        for x in range(k):
            cnt[x] += cntl[x]
            cnt[(pl * x) % k] += cntr[x]
        return Node(prod, cnt)

    def update(self, o, left, right, idx, val):
        if left == right:
            prod = val % self.k
            cnt = [0] * self.k
            cnt[prod] = 1
            self.tree[o] = Node(prod, cnt)
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

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n, m = len(nums), len(queries)
        seg = SegmentTree([x % k for x in nums], k)
        ans = [0] * m
        for i, (idx, val, start, x) in enumerate(queries):
            seg.update(1, 1, n, idx + 1, val % k)
            ans[i] = seg.query(1, 1, n, start + 1, n).cnt[x]
        return ans

sol = Solution()
print(sol.resultArray([1,2,3,4,5], 3, [[2,2,0,2],[3,3,3,0],[0,1,0,1]]))  # [2,2,2]
print(sol.resultArray([1,2,4,8,16,32], 4, [[0,2,0,2],[0,2,0,1]]))  # [1,0]
print(sol.resultArray([1,1,2,1,1], 2, [[2,1,0,1]]))  # [5]
