# @algorithm @lc id=1576 lang=python3 
# @title reorder-routes-to-make-all-paths-lead-to-the-city-zero


from en.Python3.mod.preImport import *
# @test(6,[[0,1],[1,3],[2,3],[4,0],[4,5]])=3
# @test(5,[[1,0],[1,2],[3,2],[3,4]])=2
# @test(3,[[1,0],[2,0]])=0
class Solution:
    """
        DFS紀錄正向邊數量
    """
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        edges = set()
        for u, v in connections:
            g[u].append(v)
            g[v].append(u)
            edges.add((u, v))
        ans = 0
        def dfs(u, fa):
            nonlocal ans
            for v in g[u]:
                if v != fa:
                    if (u, v) in edges:
                        ans += 1
                    dfs(v, u)
        dfs(0, -1)
        return ans