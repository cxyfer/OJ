import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        groups = defaultdict(list)
        for i, x in enumerate(nums):
            groups[x].append(i)
        ans = float('inf')
        for g in groups.values():
            if len(g) < 3:
                continue
            m = len(g)
            for i in range(m - 2):
                ans = min(ans, g[i+1] - g[i] + g[i+2] - g[i+1] + g[i+2] - g[i])
        return ans if ans != float('inf') else -1