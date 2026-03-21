#
# @lc app=leetcode id=3873 lang=python3
#
# [3873] Maximum Points Activated with One Addition
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class UnionFind:
    __slots__ = ['n', 'pa', 'sz', 'cnt']

    def __init__(self, n: int):
        self.n = n
        self.pa = list(range(n))  # 父節點
        self.sz = [1] * n  # 連通分量大小
        self.cnt = n  # 連通分量數量

    def find(self, x: int) -> int:
        while self.pa[x] != x:
            self.pa[x] = self.pa[self.pa[x]]
            x = self.pa[x]
        return x

    def union(self, x: int, y: int) -> bool:
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False
        if self.sz[fx] < self.sz[fy]:
            fx, fy = fy, fx
        self.pa[fy] = fx
        self.sz[fx] += self.sz[fy]
        self.cnt -= 1
        return True

class Solution:
    def maxActivated(self, points: list[list[int]]) -> int:
        n = len(points)
        
        mapX = defaultdict(list)
        mapY = defaultdict(list)
        for u, (x, y) in enumerate(points):
            mapX[x].append(u)
            mapY[y].append(u)

        uf = UnionFind(n)
        for lst in mapX.values():
            for u, v in pairwise(lst):
                uf.union(u, v)
        for lst in mapY.values():
            for u, v in pairwise(lst):
                uf.union(u, v)

        mx1 = mx2 = 0
        vis = [False] * n
        for u in range(n):
            fu = uf.find(u)
            if vis[fu]:
                continue
            vis[fu] = True
            sz = uf.sz[fu]
            if sz > mx1:
                mx1, mx2 = sz, mx1
            elif sz > mx2:
                mx2 = sz
        return mx1 + mx2 + 1
# @lc code=end

