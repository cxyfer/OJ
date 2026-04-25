import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *


class Solution:
    def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(nums)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        ans = 0
        # 1 <= n == nums.length <= 13
        for msk in range(1, 1 << n):
            if (sum(nums[u] for u in range(n) if (msk >> u) & 1) & 1):
                continue

            vis = [False] * n
            def dfs(u):
                vis[u] = True
                for v in g[u]:
                    if ((msk >> v) & 1 == 0) or vis[v]:
                        continue
                    dfs(v)

            lb = msk & -msk
            u = lb.bit_length() - 1
            dfs(u)
            for u in range(n):
                if (msk >> u) & 1 and not vis[u]:
                    break
            else:
                ans += 1
        return ans

sol = Solution()
print(sol.evenSumSubgraphs(nums = [1,0,1], edges = [[0,1],[1,2]]))  # 2
print(sol.evenSumSubgraphs(nums = [0,0,0], edges = [[0,1],[0,2],[1,2]]))