#
# @lc app=leetcode.cn id=924 lang=python3
#
# [924] 尽量减少恶意软件的传播
#
from preImport import *
# @lc code=start

class UnionFind:
    __slots__ = ['pa', 'size', 'count']

    def __init__(self, n: int):
        self.pa = list(range(n)) # 父節點
        self.size = [1] * n # 連通分量大小
        self.count = n # 連通分量數量

    def find(self, x: int) -> int:
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]
    
    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.size[px] < self.size[py]:
            px, py = py, px
        self.pa[py] = px
        self.size[px] += self.size[py]
        self.count -= 1
        return True

class Solution:
    """
        DSU / DFS

        由於只能移除一個初始節點，所以若一個連通分量中有多個初始節點，則移除其中之一都不影響最後的結果
        故需找只有一個初始節點的連通分量，且這個連通分量中的節點數量最多越好
        題目中 `graph[i][j] == graph[j][i]` ，所以是無向圖
    """
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        # return self.solve1(graph, initial)
        return self.solve2(graph, initial)
    """
        1. DSU
    """
    def solve1(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if graph[i][j]:
                    uf.union(i, j)
        cnt = [0] * n # 連通分量中的起始節點數量
        for x in initial:
            cnt[uf.find(x)] += 1
        ans, max_size = -1, -1
        for x in initial:
            px = uf.find(x)
            if cnt[px] > 1:
                continue
            size = uf.size[px]
            if size > max_size or (size == max_size and x < ans):
                max_size = size
                ans = x
        return ans if ans != -1 else min(initial)
    """
        2. DFS
    """
    def solve2(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)
        nodes = set(initial)
        visited = [False] * n
        cnt = [0] * n # 連通分量中的起始節點數量
        
        def dfs(u: int, st: int) -> int: # u: 當前節點, st: 起始節點, res: 連通分量大小
            res = 1
            if u in nodes: cnt[st] += 1
            visited[u] = True
            for v in range(n):
                if graph[u][v] and not visited[v]:
                    res += dfs(v, st)
            return res
        
        ans, max_size = -1, -1
        for x in initial:
            if visited[x]: # 已經訪問過
                continue
            size = dfs(x, x)
            if cnt[x] > 1: # 連通分量中有多個起始節點
                continue
            if size > max_size or (size == max_size and x < ans):
                max_size = size
                ans = x
        return ans if ans != -1 else min(initial)
# @lc code=end
sol = Solution()
print(sol.minMalwareSpread([[1,1,0],[1,1,0],[0,0,1]],[0,1,2])) # 2
print(sol.minMalwareSpread([[1,1,0],[1,1,0],[0,0,1]],[0,1])) # 0