import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
        mask = (1 << t) - 1
        f = [1] * n
        for _ in range(k):
            nf = [0] * n
            for u in range(n):
                if f[u] == 0:
                    continue
                for (v, w) in g[u]:
                    nf[v] |= (f[u] << w)
            for v in range(n):
                nf[v] &= mask
            f = nf
        ans = -1
        for v in range(n):
            ans = max(ans, f[v].bit_length() - 1)
        return ans

sol = Solution()
print(sol.maxWeight(3, [[0,1,1],[1,2,2]], 2, 4)) # 3
print(sol.maxWeight(3, [[0,1,2],[0,2,3]], 1, 3)) # 2
print(sol.maxWeight(3, [[0,1,6],[1,2,8]], 1, 6)) # -1
