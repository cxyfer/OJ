import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class SegmentTree:
    def __init__(self, nums: List[int], k: int):
        n = len(nums)
        self.n = n
        self.k = k
        self.nums = [0] + nums # 讓 index 從 1 開始
        self.tree = [[0, 0, 0] for _ in range(4 * n)] # (區間內0的數量, 區間內1的數量, 區間內符合條件子字串的數量)
        self.build(1, 1, n)
 
    def build(self, o, left, right): # node, left, right
        if left == right: # Leaf node initialization
            self.tree[o] = [0, 0, 0]
            if self.nums[left] == 1:
                self.tree[o][1] += 1
            else:
                self.tree[o][0] += 1
            self.tree[o][2] = 1 if self.tree[o][0] <= self.k or self.tree[o][1] <= self.k else 0
            return
        mid = (left + right) // 2
        self.build(2*o, left, mid) # left child
        self.build(2*o+1, mid + 1, right) # right child
        self.tree[o] = self.merge(self.tree[2*o], self.tree[2*o+1], left, mid, right)

    # 合併 [left, mid] 和 [mid+1, right] 兩部分的結果
    def merge(self, left_part, right_part, left, mid, right):
        res = [0, 0, 0]
        res[0] = left_part[0] + right_part[0]
        res[1] = left_part[1] + right_part[1]
        res[2] = left_part[2] + right_part[2]

        if res[0] <= self.k or res[1] <= self.k:
            res[2] += (mid - left + 1) * (right - mid)
            return res
        
        cnt0, cnt1 = left_part[0], left_part[1]
        l = left
        for r in range(mid + 1, right + 1): # 枚舉右端點
            if self.nums[r] == 0:
                cnt0 += 1
            else:
                cnt1 += 1
            while l <= mid and cnt0 > self.k and cnt1 > self.k:
                if self.nums[l] == 0:
                    cnt0 -= 1
                else:
                    cnt1 -= 1
                l += 1
            res[2] += mid - l + 1
        return res

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
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n = len(s)
        st = SegmentTree(list(map(int, s)), k)
        res = [0] * len(queries)
        for i, (l, r) in enumerate(queries):
            res[i] = st.query(1, 1, n, l+1, r+1)[2]
        return res
    
sol = Solution()
print(sol.countKConstraintSubstrings("0001111", 2, [[0,6]])) # [26]
print(sol.countKConstraintSubstrings("010101", 1, [[0,5],[1,4],[2,3]])) # [15,9,3]

# [101,106,88,93,76,81,65,70,60,50,41,33,26,20]
print(sol.countKConstraintSubstrings("000100000100011", 2, [[0,13],[0,14],[1,13],[1,14],[2,13],[2,14],[3,13],[3,14],[4,14],[5,14],[6,14],[7,14],[8,14],[9,14]])) # [15,9,3]