#
# @lc app=leetcode.cn id=2642 lang=python3
#
# [2642] 设计可以求最短路径的图类
#
from preImport import *
# @lc code=start
class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.g = [ [inf] *n for _ in range(n) ]
        for u, v, w in edges:
            self.g[u][v] = w

    def addEdge(self, edge: List[int]) -> None:
        u, v, w = edge
        self.g[u][v] = w

    """
        1. Dijkstra
    """
    def shortestPath(self, node1: int, node2: int) -> int:
        n = self.n
        dist = [inf] * n  # 從 start 出發，到各個點的最短路徑，如果不存在則為無窮大
        dist[node1] = 0
        visited = [False] * n
        while True:  # 至多循環 n 次
            x = -1 # 當前最短路徑，去更新它的鄰居的最短路徑
            for i, (vis, d) in enumerate(zip(visited, dist)):
                if not vis and (x < 0 or d < dist[x]):
                    x = i
            if x < 0 or dist[x] == inf:  # 所有從 start 能到達的點都被更新了
                return -1
            if x == node2:  # 找到終點，提前退出
                return dist[x]
            visited[x] = True  # 標記，在後續的循環中無需反復更新 x 到其餘點的最短路徑長度
            for y, w in enumerate(self.g[x]):
                if dist[x] + w < dist[y]:
                    dist[y] = dist[x] + w
# @lc code=end

