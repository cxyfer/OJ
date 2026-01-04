import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def minMergeCost(self, lists: List[List[int]]) -> int:
        n = len(lists)
        U = 1 << n

        md = [0] * U
        ln = [0] * U
        for msk in range(1, U):
            merged = []
            for i, lst in enumerate(lists):
                if (msk >> i) & 1:
                    merged.extend(lst)
                    ln[msk] += len(lst)
            merged.sort()
            md[msk] = merged[(ln[msk] - 1) // 2]

        @cache
        def dfs(msk):
            if (msk & (msk - 1)) == 0:
                return 0
            res = float("inf")
            sub = msk & (msk - 1)
            while sub:
                res = min(res, dfs(sub) + dfs(msk ^ sub) + ln[msk] + abs(md[sub] - md[msk ^ sub]))
                sub = (sub - 1) & msk
            return res
        return dfs(U - 1)

sol = Solution()
print(sol.minMergeCost([[1,3,5],[2,4],[6,7,8]]))  # 18