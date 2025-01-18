# @algorithm @lc id=2121 lang=python3 
# @title find-if-path-exists-in-graph


from en.Python3.mod.preImport import *
# @test(3,[[0,1],[1,2],[2,0]],0,2)=true
# @test(6,[[0,1],[0,2],[3,5],[5,4],[4,3]],0,5)=false
class Solution:
    """
        1. DFS
        2. DSU
    """
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # return self.solve1(n, edges, source, destination)
        return self.solve2(n, edges, source, destination)
    def solve1(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        visited = [False] * n
        def dfs(u: int):
            visited[u] = True
            for v in g[u]:
                if not visited[v]:
                    dfs(v)
        dfs(source)
        return visited[destination]
    def solve2(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        pa = list(range(n))
        def find(x: int) -> int:
            if x != pa[x]:
                pa[x] = find(pa[x])
            return pa[x]
        def union(x: int, y: int):
            # px, py = find(x), find(y)
            # if px != py:
            #     pa[px] = py
            pa[find(x)] = find(y)
        for u, v in edges:
            union(u, v)
        return find(source) == find(destination)