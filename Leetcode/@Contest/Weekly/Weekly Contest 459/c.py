import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

K = 6

def f(x):
    if x == 1:
        return 0
    return f(x.bit_count()) + 1

class SegmentTree:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.n = n
        self.nums = [0] + nums # 讓 index 從 1 開始
        # self.tree = [0 for _ in range(4 * n)]
        self.tree = [[0] * K for _ in range(1 << (n.bit_length() + 1))]
        self.build(1, 1, n)
 
    def build(self, o, left, right): # node, left, right
        if left == right: # Leaf node initialization
            self.tree[o] = [0] * K
            self.tree[o][self.nums[left]] += 1
            return
        mid = (left + right) // 2
        self.build(2*o, left, mid) # left child
        self.build(2*o+1, mid + 1, right) # right child
        self.tree[o] = self.merge(self.tree[2*o], self.tree[2*o+1], left, mid, right)

    # 合併 [left, mid] 和 [mid+1, right] 兩部分的結果
    def merge(self, left_part, right_part, left, mid, right):
        return [left_part[i] + right_part[i] for i in range(K)]

    def update(self, o, left, right, idx, val):
        if left == right:
            self.tree[o] = [0] * K
            self.tree[o][val] += 1
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
    def popcountDepth(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        vals = [f(x) for x in nums]
        st = SegmentTree(vals)
        ans = []
        for op, *args in queries:
            if op == 1:
                l, r, k = args
                ans.append(st.query(1, 1, len(nums), l + 1, r + 1)[k])
            else:
                i, v = args
                st.update(1, 1, len(nums), i + 1, f(v))
        return ans

sol = Solution()
print(sol.popcountDepth([2,4], [[1,0,1,1],[2,1,1],[1,0,1,0]])) # [2,1]

print(sol.popcountDepth([8], [[2,0,8],[1,0,0,2],[2,0,5],[1,0,0,4],[2,0,9],[2,0,9],[1,0,0,2],[2,0,10],[1,0,0,5],[1,0,0,0]])) # [1,1,1,1,1,1,1,1,1,1]