#
# @lc app=leetcode id=261 lang=python3
# @lcpr version=30204
#
# [261] Graph Valid Tree
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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)
        for u, v in edges:
            if not uf.union(u, v):
                return False
        return uf.cnt == 1
# @lc code=end



#
# @lcpr case=start
# 5\n[[0,1],[0,2],[0,3],[1,4]]\n
# @lcpr case=end

# @lcpr case=start
# 5\n[[0,1],[1,2],[2,3],[1,3],[1,4]]\n
# @lcpr case=end

#

