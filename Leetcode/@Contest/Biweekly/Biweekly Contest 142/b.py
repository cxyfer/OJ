import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)

        p2 = parent.copy()
        latest = defaultdict(lambda: -1)
        def dfs(u):
            ch = s[u]
            prev = latest[ch]
            if prev != -1:
                p2[u] = prev
            latest[ch] = u
            for v in g[u]:
                dfs(v)
            if prev == -1:
                del latest[ch]
            else:
                latest[ch] = prev
        dfs(0)

        g2 = [[] for _ in range(n)]
        for i in range(1, n):
            g2[p2[i]].append(i)

        ans = [0] * n
        def dfs2(u):
            res = 1
            for v in g2[u]:
                res += dfs2(v)
            ans[u] = res
            return res
        dfs2(0)
        return ans

sol = Solution()
print(sol.findSubtreeSizes([-1,0,0,1,1,1], "abaabc"))  # [6,3,1,1,1,1]
print(sol.findSubtreeSizes([-1,0,4,0,1], "abbba"))  # [5,2,1,1,1]