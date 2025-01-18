#
# @lc app=leetcode.cn id=1466 lang=python3
#
# [1466] 重新规划路线
#
from preImport import *
# @lc code=start
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
# @lc code=end

