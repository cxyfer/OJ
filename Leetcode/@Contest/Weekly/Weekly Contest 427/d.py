import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
import sys
import bisect
from collections import defaultdict

import sys
import bisect
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

class SegNode:
    def __init__(self):
        self.ls = self.rs = None
        self.val = 0

    def copy(self):
        node = SegNode()
        node.ls = self.ls
        node.rs = self.rs
        node.val = self.val
        return node

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.roots = [SegNode()]

    def build(self, A):
        for x in A:
            self.roots.append(self.insert(self.roots[-1], 1, self.n, x))

    def insert(self, prev, left, right, v):
        node = prev.copy()
        if left == right:
            node.val += 1
            return node
        mid = (left + right) // 2
        if v <= mid:
            if prev.ls is None:
                prev.ls = SegNode()
            node.ls = self.insert(prev.ls, left, mid, v)
        else:
            if prev.rs is None:
                prev.rs = SegNode()
            node.rs = self.insert(prev.rs, mid + 1, right, v)
        self.pushup(node)
        return node
    
    def pushup(self, node):
        node.val = (0 if node.ls is None else node.ls.val) + (0 if node.rs is None else node.rs.val)

    def _query(self, node, left, right, l, r):
        if node is None:
            return 0
        if l <= left and right <= r:
            return node.val
        mid = (left + right) // 2
        res = 0
        if l <= mid:
            res += self._query(node.ls, left, mid, l, r)
        if r > mid:
            res += self._query(node.rs, mid + 1, right, l, r)
        return res

    def query_version(self, version, l, r):
        if l > r:
            return 0
        return self._query(self.roots[version], 1, self.n, l, r)

class Solution:
    def maxRectangleArea(self, xCoord, yCoord):
        points = list(zip(xCoord, yCoord))

        # 依照 x 座標排序
        points.sort(key=lambda p: p[0])
        xArr = [p[0] for p in points]

        # 離散化 y 座標
        ySorted = sorted(set([p[1] for p in points]))
        yMap = {y : i for i,y in enumerate(ySorted, 1)}

        # 可持久化線段樹
        seg = SegmentTree(len(ySorted))
        seg.build([yMap[y] for _, y in points])

        # 分組
        mp_y = defaultdict(list)
        for x, y in points:
            mp_y[y].append(x)
        
        mp_p = defaultdict(list)
        for y, Xs in mp_y.items():
            Xs.sort()
            for i in range(len(Xs)):
                for j in range(i + 1, len(Xs)):
                    x1, x2 = Xs[i], Xs[j]
                    mp_p[(x1, x2)].append(y)
    
        # 遍歷所有可能的矩形
        ans = -1
        for (x1, x2), Ys in mp_p.items():
            Ys.sort()
            for y1, y2 in pairwise(Ys):
                v1 = bisect_left(xArr, x1)  
                v2 = bisect_right(xArr, x2)
                cnt = seg.query_version(v2, yMap[y1], yMap[y2]) - seg.query_version(v1, yMap[y1], yMap[y2])
                if cnt == 4:
                    ans = max(ans, (x2 - x1) * (y2 - y1))
        return ans
    
sol = Solution()
print(sol.maxRectangleArea([1,1,3,3],[1,3,1,3])) # 4
print(sol.maxRectangleArea([1,1,3,3,2],[1,3,1,3,2])) # -1
print(sol.maxRectangleArea([1,1,3,3,1,3],[1,3,1,3,2,2])) # 2
print(sol.maxRectangleArea([89,55,89,55,0,34,17,71,98,90,63,49,76,72,4,46,67,94,52,6],[58,69,69,58,100,36,14,40,13,41,29,23,47,52,95,49,37,77,54,59])) # 374