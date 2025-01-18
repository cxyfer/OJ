#
# @lc app=leetcode id=3244 lang=python3
# @lcpr version=30204
#
# [3244] Shortest Distance After Road Addition Queries II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class UnionFind():
    __slots__ = ['pa', 'cnt'] 

    def __init__(self, n):
        self.pa = list(range(n))
        self.cnt = n

    def find(self, x):
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]
    
    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return
        if fx < fy: # 按照右端點合併
            fx, fy = fy, fx
        self.pa[fy] = fx
        self.cnt -= 1

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        m = len(queries)
        uf = UnionFind(n - 1)
        ans = [-1] * m
        for i, (l, r) in enumerate(queries):
            idx = uf.find(l)
            while idx < r - 1:
                uf.union(idx, idx + 1)
                idx = uf.find(idx)
            ans[i] = uf.cnt
        return ans
# @lc code=end



#
# @lcpr case=start
# 5\n[[2,4],[0,2],[0,4]]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[[0,3],[0,2]]\n
# @lcpr case=end

#

