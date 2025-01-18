import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class SegmentTree:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.n = n
        self.nums = [0] + nums # 讓 index 從 1 開始
        self.tree = [0 for _ in range(4 * n)]
        self.build(1, 1, n)
 
    def build(self, o, left, right): # node, left, right
        if left == right: # Leaf node initialization
            self.tree[o] = 0
            return
        mid = (left + right) // 2
        self.build(2*o, left, mid) # left child
        self.build(2*o+1, mid + 1, right) # right child
        self.tree[o] = self.merge(self.tree[2*o], self.tree[2*o+1], left, mid, right)
    """
        合併 [left, mid] 和 [mid+1, right] 兩部分的結果
    """
    def merge(self, left_part, right_part, left, mid, right):
        res = left_part + right_part
        if right - left < 2:
            return res
        if (mid - 1 >= left and self.nums[mid-1] < self.nums[mid] > self.nums[mid+1]) \
            or (mid + 2 <= right and self.nums[mid] < self.nums[mid+1] > self.nums[mid+2]):
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
 
class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        seg = SegmentTree(nums)
        ans = []
        for op, *args in queries:
            if op == 1:
                l, r = args
                # print(seg.nums)
                ans.append(seg.query(1, 1, n, l+1, r+1))
            else:
                idx, val = args
                seg.update(1, 1, n, idx+1, val)
        return ans
                
sol = Solution()
print(sol.countOfPeaks([3,1,4,2,5], [[2,3,4],[1,0,4]])) # [0]
print(sol.countOfPeaks([4,1,4,2,1,5], [[2,2,4],[1,0,2],[1,0,4]])) # [0,1]
print(sol.countOfPeaks([4,5,5], [[1,2,2],[1,0,1],[1,1,2]])) # [0, 0, 0]
print(sol.countOfPeaks([7,10,7], [[1,2,2],[2,0,6],[1,0,2]])) # [0, 1]
print(sol.countOfPeaks([4,8,7,7,6,9], [[1,5,5],[1,2,4],[1,0,0]])) # [0, 0, 0]

print(sol.countOfPeaks([10,5,10,3,7], [[2,4,2],[1,1,4],[1,1,3],[1,2,2]])) # [1, 1, 0]
print(sol.countOfPeaks([9,7,5,8,9], [[2,0,2],[1,0,3],[1,3,3],[2,3,5]])) # [1, 0]
print(sol.countOfPeaks([4,10,10,5,8,5,6,4,7,10], [[2,5,8],[1,5,7],[2,8,1],[2,0,4]])) # [0]