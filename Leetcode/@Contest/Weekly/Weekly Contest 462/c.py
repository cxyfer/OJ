import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        g = defaultdict(list)
        for v, l in zip(value, limit):
            g[l].append(v)
        ans = 0
        for l, vals in g.items():
            vals.sort(reverse = True)
            ans += sum(vals[:l])
        return ans

sol = Solution()
print(sol.maxTotal([3,5,8], [2,1,3]))  # 16
print(sol.maxTotal([4,2,6], [1,1,1]))  # 6
print(sol.maxTotal([4,1,5,2], [3,3,2,3]))  # 12
print(sol.maxTotal([20356,98764,60422,22268], [4,3,2,2]))  # 201810