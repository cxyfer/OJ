# @algorithm @lc id=3389 lang=python3 
# @title minimum-time-to-visit-disappearing-nodes


from en.Python3.mod.preImport import *
# @test(3,[[0,1,2],[1,2,1],[0,2,4]],[1,1,5])=[0,-1,4]
# @test(3,[[0,1,2],[1,2,1],[0,2,4]],[1,3,5])=[0,2,3]
# @test(2,[[0,1,1]],[1,1])=[0,-1]
# @test(2,[[0,1,1]], [1,1])=[0,-1]
class Solution:
    """
        Dijkstra
        在一般的SSSP之上，加入了節點會在特定時間點後消失的限制條件。
        因此在更新節點時，要檢查節點是否已經消失，若已經消失則不能用該節點去更新其他節點。
        需要注意若到達時間和消失時間相同，是先消失，故不能到達該節點。
    """
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))
        
        dist = [float("inf")] * n
        dist[0] = 0
        hp = [(0, 0)]
        while hp:
            d, u = heappop(hp)
            if d > dist[u]: # lazy deletion
                continue
            for v, w in g[u]:
                nd = d + w # new distance
                if nd >= disappear[v]: # 在到達 v 的時候， v 已經消失了，故不能用 v 去更新其他節點
                    continue
                if nd < dist[v]: # 從 u 到達 v 的時間比原來紀錄的時間更短
                    dist[v] = nd
                    heappush(hp, (nd, v)) # lazy insertion
        ans = [d if d != float("inf") else -1 for d in dist]
        return ans