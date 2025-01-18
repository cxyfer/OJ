#
# @lc app=leetcode.cn id=787 lang=python3
#
# [787] K 站中转内最便宜的航班
#
from preImport import *
# @lc code=start
class Solution:
    """
        1. BFS + Pruning
        2. Dynamic Programming
        3. Bellman-Ford
        4. Bellman-Ford without building graph

        https://leetcode.cn/problems/cheapest-flights-within-k-stops/solutions/956113/tong-ge-lai-shua-ti-la-yi-ti-si-jie-bfs-deqpt
    """
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # return self.solve1(n, flights, src, dst, k)
        # return self.solve2(n, flights, src, dst, k)
        # return self.solve3(n, flights, src, dst, k)
        return self.solve4(n, flights, src, dst, k)
    """
        1. BFS + Pruning

        Time: O(k * n^2)
        Space: O(n)
    """
    def solve1(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = [[float("inf")] * n for _ in range(n)] # Build graph
        adj = defaultdict(list)
        for u, v, w in flights:
            g[u][v] = min(g[u][v], w)
            adj[u].append(v)

        dist = [float('inf')] * n # Initialize distance
        dist[src] = 0

        q = deque([(src, 0, 0)]) # BFS
        while q:
            u, d, s = q.popleft()
            if s > k: # Pruning
                break
            for v in adj[u]:
                if dist[v] > d + g[u][v]:
                    dist[v] = d + g[u][v]
                    q.append((v, dist[v], s+1))
        return dist[dst] if dist[dst] != float('inf') else -1
    """
        2. Dynamic Programming
        dp[i][k] 表示 在 k 步內，從 src 到 i 的最小花費
        經過 k 個中轉站，即 k+1 步 (包含終點)
        可以看到 dp[i][k] 只和 dp[i][k-1] 有關，所以可以優化成一維陣列

        Time: O((n+m)k)
        Space: O(nk)
    """
    def solve2(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [[float("inf")] * (k + 2) for _ in range(n)] # k+2 是因為 k+1 步 (包含終點)
        dp[src][0] = 0

        for t in range(1, k + 2):
            for u, v, w in flights:
                dp[v][t] = min(dp[v][t], dp[u][t-1] + w)
        ans = min(dp[dst][t] for t in range(1, k + 2))
        return -1 if ans == float("inf") else ans
    """
        3. Bellman-Ford
    """
    def solve3(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = [[float("inf")] * n for _ in range(n)]
        for u, v, w in flights:
            g[u][v] = min(g[u][v], w)

        dist = [float('inf')] * n
        dist[src] = 0

        while k >= 0:
            clone = dist[:]
            for i in range(n):
                for j in range(n):
                    if clone[i] + g[i][j] < dist[j]:
                        dist[j] = clone[i] + g[i][j]
            k -= 1
        return -1 if dist[dst] == float("inf") else dist[dst]
    """
        4. Bellman-Ford without building graph
    """
    def solve4(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')] * n
        dist[src] = 0

        while k >= 0:
            clone = dist[:]
            for u, v, w in flights:
                if clone[u] + w < dist[v]:
                    dist[v] = clone[u] + w
            k -= 1
        return -1 if dist[dst] == float("inf") else dist[dst]
# @lc code=end
sol = Solution()

# print(sol.findCheapestPrice(4,[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],0,3,1)) # 700
# print(sol.findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,1)) # 200
# print(sol.findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,0)) # 500
print(sol.findCheapestPrice(4, [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], 0, 3, 1)) # 6
