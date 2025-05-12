#
# @lc app=leetcode id=3547 lang=python3
#
# [3547] Maximum Sum of Edge Values in a Graph
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
    def maxScore(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        deg = [0] * n
        for x, y in edges:
            deg[x] += 1
            deg[y] += 1
            uf.union(x, y)
        
        sizes = [0] * n
        is_ring = [True] * n
        for u in range(n):
            fu = uf.find(u)
            sizes[fu] += 1
            if deg[u] & 1:
                is_ring[fu] = False
        rings = []
        chains = []
        for u in range(n):
            fu = uf.find(u)
            if sizes[fu] == 0:
                continue
            if is_ring[fu] and sizes[fu] >= 3:
                rings.append(sizes[fu])
            else:
                chains.append(sizes[fu])
            sizes[fu] = 0
        
        rings.sort(reverse=True)
        chains.sort(reverse=True)

        ans = 0
        k = n
        for sz in rings:
            assert sz >= 3
            cur = [k, k - 1]
            ans += cur[0] * cur[1]
            k -= 2
            for i in range(sz - 2):
                ans += cur[i & 1] * k
                cur[i & 1] = k
                k -= 1
            ans += cur[0] * cur[1]

        for sz in chains:
            if sz == 1:
                continue
            cur = [k, k - 1]
            ans += cur[0] * cur[1]
            k -= 2
            for i in range(sz - 2):
                ans += cur[i & 1] * k
                cur[i & 1] = k
                k -= 1
        return ans
# @lc code=end

sol = Solution()
# print(sol.maxScore(7, [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6]])) # 130
# print(sol.maxScore(8, [[4,7],[2,1]])) # 82
print(sol.maxScore(20, [[18,14],[12,18],[12,9],[1,9],[7,1],[5,7],[0,13],[6,0],[6,16],[15,16],[10,19],[17,4],[2,4],[2,3],[3,8]])) # 2517

