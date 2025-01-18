# @algorithm @lc id=1431 lang=python3 
# @title all-ancestors-of-a-node-in-a-directed-acyclic-graph


from en.Python3.mod.preImport import *
# @test(8,[[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]])=[[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]
# @test(5,[[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]])=[[],[0],[0,1],[0,1,2],[0,1,2,3]]
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)

        def dfs(st:int, x: int) -> None:
            for y in g[x]:
                if not visited[y]:
                    visited[y] = True
                    ans[y].append(st)
                    dfs(st, y)

        ans = [[] for _ in range(n)]
        for st in range(n):
            visited = [False] * n
            dfs(st, st)
        return ans