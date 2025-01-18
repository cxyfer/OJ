# @algorithm @lc id=1887 lang=python3 
# @title minimum-degree-of-a-connected-trio-in-a-graph


from en.Python3.mod.preImport import *
# @test(6,[[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]])=3
# @test(7,[[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]])=0
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        # 暴力枚舉
        graph = [[0] * (n + 1) for _ in range(n + 1)]
        degrees = [0] * (n + 1)
        for u, v in edges:
            graph[u][v] = graph[v][u] = 1
            degrees[u] += 1
            degrees[v] += 1
        ans = math.inf
        # 枚舉每個三元組
        for i in range(1, n + 1):
            if degrees[i] < 2: continue
            if ans == 0: break
            for j in range(i + 1, n + 1):
                if graph[i][j]:
                    for k in range(j + 1, n + 1):
                        if graph[i][k] and graph[j][k]:
                            ans = min(ans, degrees[i] + degrees[j] + degrees[k] - 6)
        return ans if ans != math.inf else -1