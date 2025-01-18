#
# @lc app=leetcode.cn id=1971 lang=python3
#
# [1971] 寻找图中是否存在路径
#
from preImport import *
# @lc code=start
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
# @lc code=end

