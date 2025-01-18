#
# @lc app=leetcode id=685 lang=python3
# @lcpr version=30204
#
# [685] Redundant Connection II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
假設多的邊為 (u, v) ，則有以下 3 種情況：
1. v 是根節點，此時會出現環，但 v 只有 1 個父節點
2. v 是 u 除了根節點以外的某個祖先，此時會出現環，且 v 存在 2 個父節點
3. 其餘情況，此時 v 會有 2 個父節點
"""
class UnionFind:
    __slots__ = ['n', 'pa', 'sz']

    def __init__(self, n: int):
        self.n = n
        self.pa = list(range(n)) # 父節點
        self.sz = [1] * n # 連通分量大小

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
        return True
    
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        rg = [[] for _ in range(n + 1)] # 反圖
        mark = -1 # 記錄有兩個父節點的節點
        for idx, (u, v) in enumerate(edges):
            rg[v].append(idx) # 記錄節點 v 的邊索引
            # 出現 Case 2 或 Case 3
            if len(rg[v]) == 2:
                mark = v
        uf = UnionFind(n + 1)
        for i, (u, v) in enumerate(edges):
            # 出現 Case 2 或 Case 3，此時跳過指向 mark 的第二條邊
            if mark != -1 and i == rg[mark][1]:
                continue
            if not uf.union(u, v): # 有環
                if mark == -1: # Case 1
                    return edges[i]
                else: # Case 2a
                    return edges[rg[mark][0]]
        # Case 2b or Case 3
        return edges[rg[mark][1]]
# @lc code=end

sol = Solution()
print(sol.findRedundantDirectedConnection([[1,2],[1,3],[2,3]])) # [2,3]
print(sol.findRedundantDirectedConnection([[1,2],[2,3],[3,4],[4,1],[1,5]])) # [4,1]

print(sol.findRedundantDirectedConnection([[2,1],[3,1],[4,2],[1,4]])) # [2,1]

#
# @lcpr case=start
# [[1,2],[1,3],[2,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[2,3],[3,4],[4,1],[1,5]]\n
# @lcpr case=end

#

