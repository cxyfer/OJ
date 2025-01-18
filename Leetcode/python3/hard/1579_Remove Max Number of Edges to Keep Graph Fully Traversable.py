#
# @lc app=leetcode id=1579 lang=python3
# @lcpr version=30204
#
# [1579] Remove Max Number of Edges to Keep Graph Fully Traversable
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class DSU: # Disjoint Set Union
    __slots__ = ['n', 'pa', 'sz', 'cnt']

    def __init__(self, n: int):
        self.n = n
        self.pa = list(range(n)) # 父節點
        self.sz = [1] * n # 連通分量大小
        self.cnt = n # 連通分量數量

    def find(self, x: int) -> int:
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]
    
    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.sz[px] < self.sz[py]:
            px, py = py, px
        self.pa[py] = px
        self.sz[px] += self.sz[py]
        self.cnt -= 1
        return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        lst = [[] for _ in range(3)]
        for t, u, v in edges:
            lst[t-1].append((u-1, v-1))
        ans = 0
        uf1, uf2 = DSU(n), DSU(n)
        for u, v in lst[2]: # Common
            if not uf1.union(u, v) or not uf2.union(u, v):
                ans += 1
        for u, v in lst[0]: # Alice
            if not uf1.union(u, v):
                ans += 1
        for u, v in lst[1]: # Bob
            if not uf2.union(u, v):
                ans += 1
        return ans if uf1.cnt == 1 and uf2.cnt == 1 else -1
# @lc code=end



#
# @lcpr case=start
# 4\n[[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[[3,1,2],[3,2,3],[1,1,4],[2,1,4]]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[[3,2,3],[1,1,2],[2,3,4]]\n
# @lcpr case=end

#

