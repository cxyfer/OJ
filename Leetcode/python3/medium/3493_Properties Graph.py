#
# @lc app=leetcode id=3493 lang=python3
#
# [3493] Properties Graph
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class UnionFind:
    __slots__ = ['n', 'pa', 'sz', 'cnt']

    def __init__(self, n: int):
        self.n = n
        self.pa = list(range(n)) # 父節點
        self.sz = [1] * n # 連通分量大小
        self.cnt = n # 連通分量數量

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
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n, m = len(properties), len(properties[0])
        uf = UnionFind(n)
        sets = [set(row) for row in properties]
        for i in range(n):
            for j in range(i + 1, n):
                if len(sets[i] & sets[j]) >= k:
                    uf.union(i, j)
        return uf.cnt
# @lc code=end

