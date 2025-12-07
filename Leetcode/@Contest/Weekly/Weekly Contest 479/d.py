import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
# Q4. 換根 DP

顯然當我們固定節點 0 為根時，可以求出以 v 為子樹根節點的子樹的最大得分 f[v]，此時可以得 ans[0] = f[0]
接著考慮將根從 u 轉移到 v ，此時 u 對 v 的貢獻為 ans[u] 減去 v 對 u 的貢獻 (如有)，即 ans[u] - max(f[v], 0)
考慮對 v 來說是否需要 u 的貢獻，得 ans[v] = f[v] + max(0, ans[u] - max(f[v], 0))
"""

class Solution:
    def maxSubgraphScore(self, n: int, edges: List[List[int]], good: List[int]) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        ans = [0] * n
        f = [0] * n
        def dfs(u: int, fa: int) -> None:
            f[u] = 1 if good[u] else -1
            for v in g[u]:
                if v == fa:
                    continue
                dfs(v, u)
                f[u] += max(0, f[v])
        dfs(0, -1)
        ans[0] = f[0]
        
        def reroot(u: int, fa: int) -> None:
            for v in g[u]:
                if v == fa:
                    continue
                ans[v] = f[v] + max(0, ans[u] - max(f[v], 0))
                reroot(v, u)
        reroot(0, -1)
        return ans