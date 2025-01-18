import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:

        def check(edges):
            n = len(edges) + 1
            if n == 1:
                return 1
            if n == 2:
                return 2
            g = defaultdict(list)
            deg = [0] * n
            for u, v in edges:
                g[u].append(v)
                g[v].append(u)
                deg[u] += 1
                deg[v] += 1

            if all(x == 1 for x in deg):
                return 2
            
            res = 0
            q = deque()
            cnt = n
            for i in range(n):
                if deg[i] == 1:
                    q.append(i)
                    cnt -= 1
            while q:
                for _ in range(len(q)):
                    u = q.popleft()
                    for v in g[u]:
                        deg[v] -= 1
                        if deg[v] == 1:
                            q.append(v)
                            cnt -= 1
                res += 1
            return res
        cnt1 = check(edges1)
        cnt2 = check(edges2)
        print(cnt1, cnt2)
        return cnt1 + cnt2 - 1

sol = Solution()
print(sol.minimumDiameterAfterMerge([[0,1],[0,2],[0,3]], [[0,1]])) # 3
print(sol.minimumDiameterAfterMerge([[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]])) # 5
print(sol.minimumDiameterAfterMerge([], [])) # 1
print(sol.minimumDiameterAfterMerge([[1,0],[2,3],[1,4],[2,1],[2,5]], [[4,5],[2,6],[3,2],[4,7],[3,4],[0,3],[1,0],[1,8]])) # 6