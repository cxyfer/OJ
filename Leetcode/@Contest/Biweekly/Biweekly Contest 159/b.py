import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        n = len(coords)
        if n < 3:
            return -1

        map_x = defaultdict(list)
        map_y = defaultdict(list)
        min_x = min_y = float("inf")
        max_x = max_y = float("-inf")
        for x, y in coords:
            map_x[x].append(y)
            map_y[y].append(x)
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

        def f(mp, mx, mn):
            res = float("-inf")
            for x, ys in mp.items():
                if len(ys) < 2:
                    continue
                h = max(ys) - min(ys)
                w = max(mx - x, x - mn)
                res = max(res, h * w)
            return res
        ans = max(f(map_x, max_x, min_x), f(map_y, max_y, min_y))
        return ans if ans > 0 else -1

sol = Solution()
print(sol.maxArea([[1,1],[1,2],[3,2],[3,3]]))  # 2
print(sol.maxArea([[1,1],[2,2],[3,3]]))  # -1









