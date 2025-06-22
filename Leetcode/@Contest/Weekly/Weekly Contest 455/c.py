import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        ans = 0
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(u, fa):
            res = cost[u]
            childs = []
            for v in g[u]:
                if v == fa:
                    continue
                childs.append(dfs(v, u))
            if not childs:
                return res
            nonlocal ans
            mx = max(childs)
            ans += sum(1 for c in childs if c < mx)
            return res + mx
        dfs(0, -1)
        return ans
            
sol = Solution()
print(sol.minIncrease(3, [[0,1],[0,2]], [2,1,3])) # 1