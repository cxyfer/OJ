# There exists an undirected tree rooted at node 0 with n nodes labeled from 0 to n - 1. You are given a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree. You are also given a 0-indexed array coins of size n where coins[i] indicates the number of coins in the vertex i, and an integer k.

# Starting from the root, you have to collect all the coins such that the coins at a node can only be collected if the coins of its ancestors have been already collected.

# Coins at nodei can be collected in one of the following ways:

# Collect all the coins, but you will get coins[i] - k points. If coins[i] - k is negative then you will lose abs(coins[i] - k) points.
# Collect all the coins, but you will get floor(coins[i] / 2) points. If this way is used, then for all the nodej present in the subtree of nodei, coins[j] will get reduced to floor(coins[j] / 2).
# Return the maximum points you can get after collecting the coins from all the tree nodes.

from typing import List
from collections import deque

class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(coins)
        M = [[] for _ in range(n)]
        for u, v in edges:
            M[u].append(v)
            M[v].append(u)
        visited = [False for _ in range(n)]
        coins_bak = coins.copy()
        def dfs(u, useMethod2=False):
            res = coins[u] - k if not useMethod2 else coins[u] // 2
            # print(u, useMethod2, res)
            visited[u] = True
            for v in M[u]:
                if not visited[v]:
                    if useMethod2:
                        coins[v] /= 2
                    res1 = dfs(v)
                    visited[v] = False
                    res2 = dfs(v, True)
                    visited[v] = False  
                    res += max(res1, res2)
            return res
        res1 = dfs(0)
        visited = [False for _ in range(n)]
        coins = coins_bak.copy()
        res2 = dfs(0, True)
        # print(res1, res2)
        ans = max(res1, res2)
        return int(ans)

sol = Solution()
print(sol.maximumPoints([[0,1],[1,2],[2,3]], [10,10,3,3], 5)) # 11
print(sol.maximumPoints([[0,1],[0,2]], [8,4,4], 0)) # 16

print(sol.maximumPoints([[0,1],[0,2],[3,2],[0,4]], [5,6,8,7,4], 7)) # 8
print(sol.maximumPoints([[1,0],[2,1],[3,1]], [8,2,7,1], 2)) # 11
print(sol.maximumPoints([[0,1],[0,2],[0,3],[2,4],[5,4],[6,0],[4,7],[8,5]], [2,3,10,0,0,2,7,3,9], 2)) # 20

[[0,1],[0,2],[1,3],[3,4],[0,5],[6,3],[5,7],[3,8],[9,7]]
[0,5,10,5,6,5,0,2,0,0]
7
print(sol.maximumPoints([[0,1],[0,2],[1,3],[3,4],[0,5],[6,3],[5,7],[3,8],[9,7]], [0,5,10,5,6,5,0,2,0,0], 7)) # 4