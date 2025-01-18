#
# @lc app=leetcode.cn id=310 lang=python3
#
# [310] 最小高度树
#
from preImport import *
# @lc code=start
class Solution:
    """
        由 Leaf 開始 BFS
    """
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return list(range(n))
        g = [[] for _ in range(n)]
        deg = [0] * n
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
            deg[u] += 1
            deg[v] += 1
        q = deque([i for i in range(n) if deg[i] == 1]) # Leaf
        while q:
            ans = []
            for _ in range(len(q)):
                u = q.popleft()
                ans.append(u)
                for v in g[u]:
                    deg[v] -= 1
                    if deg[v] == 1:
                        q.append(v)  
        return ans
# @lc code=end

