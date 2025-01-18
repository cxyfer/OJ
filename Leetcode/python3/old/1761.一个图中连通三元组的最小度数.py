#
# @lc app=leetcode.cn id=1761 lang=python3
#
# [1761] 一个图中连通三元组的最小度数
#
from en.Python3.mod.preImport import *
# @lc code=start
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
# @lc code=end

