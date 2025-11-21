import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *
import typing

class SegNode:
    def __init__(self) -> None:
        self.ls = self.rs = None  # left and right child
        self.val = 0  # value
        self.lazy = 0  # lazy tag

class SegmentTree:
    def __init__(self, nums: List[int] = None):
        if isinstance(nums, int):
            nums = [0] * nums
        self.n = len(nums)
        self.root = SegNode()
        if nums is not None and len(nums) > 0:
            self.build(self.root, 1, self.n, nums)

    def update(self, l: int, r: int, v: int) -> None:
        self._update(self.root, 1, self.n, l, r, v)

    def query(self, l: int, r: int) -> int:
        return self._query(self.root, 1, self.n, l, r)

    def build(self, node: SegNode, left: int, right: int, nums: List[int]) -> None:
        if left == right:
            node.val = nums[left - 1]
            return
        mid = (left + right) // 2
        node.ls = SegNode()
        node.rs = SegNode()
        self.build(node.ls, left, mid, nums)
        self.build(node.rs, mid + 1, right, nums)
        self.pushup(node)  # push up node value

    # update the range [l, r] with value v
    def _update(self, node: SegNode, left: int, right: int, l: int, r: int, v: int) -> None:
        if l <= left and right <= r:
            # apply lazy tag
            self.apply(node, left, right, v)
            return
        self.pushdown(node, left, right)  # push down lazy tags
        mid = (left + right) // 2
        if l <= mid:
            self._update(node.ls, left, mid, l, r, v)
        if r > mid:
            self._update(node.rs, mid + 1, right, l, r, v)
        self.pushup(node)  # push up node value

    # apply lazy tag
    def apply(self, node: SegNode, left: int, right: int, v: int) -> None:
        node.val += v * (right - left + 1)
        node.lazy += v

    # query the range [l, r]
    def _query(self, node: SegNode, left: int, right: int, l: int, r: int) -> int:
        if l <= left and right <= r:
            return node.val
        # Ensure all lazy tags have been pushed down
        self.pushdown(node, left, right)
        mid = (left + right) // 2
        ans = 0
        if l <= mid:
            ans += self._query(node.ls, left, mid, l, r)
        if r > mid:
            ans += self._query(node.rs, mid + 1, right, l, r)
        return ans

    # push down lazy tags
    def pushdown(self, node: SegNode, left: int, right: int) -> None:
        if node.ls is None:
            node.ls = SegNode()
        if node.rs is None:
            node.rs = SegNode()
        if node.lazy != 0:
            # apply lazy tag
            mid = (left + right) // 2
            self.apply(node.ls, left, mid, node.lazy)
            self.apply(node.rs, mid + 1, right, node.lazy)
            node.lazy = 0  # reset lazy tag

    # push up node value
    def pushup(self, node: SegNode) -> None:
        # update node value
        node.val = node.ls.val + node.rs.val

class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)

        qs = [[] for _ in range(n + 1)]  # 將詢問按照右端點分組
        for qid, (l, r) in enumerate(queries):
            qs[r + 1].append((qid, l + 1))  # 1-based
            
        # tree[i] 表示以 i 為左端點的穩定子陣列數量
        seg = SegmentTree(n)

        ans = [0] * len(queries)
        st = 0  # 每個非遞減段的開頭
        prev = float('inf')  
        for r, x in enumerate(nums, start=1):  # 枚舉右端點
            if prev > x:
                st = r
            prev = x

            seg.update(l=st, r=r, v=1)  # 當前的右端點，會對 tree[st] ~ tree[r] 產生 1 的貢獻
            for qid, l in qs[r]:
                ans[qid] = seg.query(l=l, r=r)
        return ans

sol = Solution()
print(sol.countStableSubarrays([3,1,2], [[0,1],[1,2],[0,2]]))  # [2,3,4]
print(sol.countStableSubarrays([2,2], [[0,1],[0,0]]))  # [3,1]
print(sol.countStableSubarrays([7,6,16], [[2,2]]))  # [1]