import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:

        def diameter(edges):
            n = len(edges) + 1
            g = [[] for _ in range(n)]
            for u, v in edges:
                g[u].append(v)
                g[v].append(u)
            res = 0
            def dfs(u, fa):
                nonlocal res
                max1 = max2 = 0
                for v in g[u]:
                    if v != fa:
                        mx = dfs(v, u) + 1
                        if mx >= max1:
                            max2 = max1
                            max1 = mx
                        elif mx >= max2:
                            max2 = mx
                        res = max(res, max1 + max2)
                return max1
            dfs(0, -1)
            return res
        
        d1 = diameter(edges1)
        d2 = diameter(edges2)
        ans = (d1 + 1) // 2 + (d2 + 1) // 2 + 1
        # return ans
        return max(ans, d1, d2) # 忘了考慮原本的直徑，我是白癡 = =

sol = Solution()
print(sol.minimumDiameterAfterMerge([[0,1],[0,2],[0,3]], [[0,1]])) # 3
print(sol.minimumDiameterAfterMerge([[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]])) # 5
print(sol.minimumDiameterAfterMerge([], [])) # 1
print(sol.minimumDiameterAfterMerge([[1,0],[2,3],[1,4],[2,1],[2,5]], [[4,5],[2,6],[3,2],[4,7],[3,4],[0,3],[1,0],[1,8]])) # 6


print(sol.minimumDiameterAfterMerge([[0,1],[2,0],[3,2],[3,6],[8,7],[4,8],[5,4],[3,5],[3,9]], [[0,1],[0,2],[0,3]])) # 7
