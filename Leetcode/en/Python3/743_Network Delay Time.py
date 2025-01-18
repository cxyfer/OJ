# @algorithm @lc id=744 lang=python3 
# @title network-delay-time


from en.Python3.mod.preImport import *
# @test([[2,1,1],[2,3,1],[3,4,1]],4,2)=2
# @test([[1,2,1]],2,1)=1
# @test([[1,2,1]],2,2)=-1
class Solution:
    """
        Dijkstra 模板題 with Priority Queue
    """
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = [[] for _ in range(n)]
        for u, v, w in times:
            g[u - 1].append((v - 1, w))
        
        dist = [float("inf")] * n
        dist[k - 1] = 0
        hp = [(0, k - 1)]
        while hp:
            d, u = heappop(hp)
            if d > dist[u]: # lazy deletion
                continue
            for v, w in g[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heappush(hp, (nd, v)) # lazy insertion
        ans = max(dist)
        return ans if ans != float("inf") else -1