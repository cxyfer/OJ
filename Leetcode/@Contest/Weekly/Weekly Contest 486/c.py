import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def get_dist(u):
            dist = [float('inf')] * n
            dist[u] = 0
            q = deque([u])
            while q:
                u = q.popleft()
                for v in g[u]:
                    if dist[u] + 1 < dist[v]:
                        dist[v] = dist[u] + 1
                        q.append(v)
            return dist

        ans = 0
        for a, b, c in zip(get_dist(x), get_dist(y), get_dist(z)):
            a, b, c = sorted([a, b, c])
            if a * a + b * b == c * c:
                ans += 1
        return ans