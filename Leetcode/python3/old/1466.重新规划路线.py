#
# @lc app=leetcode.cn id=1466 lang=python3
#
# [1466] 重新规划路线
#
from typing import *
# @lc code=start
class Solution:
    """
        DFS紀錄正向邊數量
    """
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False for _ in range(n)]
        direct = set() # 保存有向邊
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
            direct.add((u, v))
        ans = 0
        def dfs(u):
            nonlocal ans
            visited[u] = True
            for v in adj[u]:
                if not visited[v]:
                    if (u, v) in direct: # 即這條邊在原圖上是正向邊
                        ans += 1
                    dfs(v)
        dfs(0)
        return ans
# @lc code=end

