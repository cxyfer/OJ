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