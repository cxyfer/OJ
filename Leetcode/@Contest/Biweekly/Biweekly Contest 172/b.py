import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        gs = [[] for _ in range(3)]
        for x in nums:
            gs[x % 3].append(x)
        for g in gs:
            g.sort(reverse=True)
        ans = 0
        if len(gs[0]) >= 3:
            ans = max(ans, sum(gs[0][:3]))
        if len(gs[0]) >= 1 and len(gs[1]) >= 1 and len(gs[2]) >= 1:
            ans = max(ans, gs[0][0] + gs[1][0] + gs[2][0])
        if len(gs[1]) >= 3:
            ans = max(ans, sum(gs[1][:3]))
        if len(gs[2]) >= 3:
            ans = max(ans, sum(gs[2][:3]))
        return ans