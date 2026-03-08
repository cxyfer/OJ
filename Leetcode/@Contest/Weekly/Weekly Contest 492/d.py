import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
        n = len(s)
        ss = list(accumulate(map(int, s), initial=0))

        def dfs(l: int, r: int) -> int:
            ln = r - l + 1
            x = ss[r + 1] - ss[l]
            res = (ln * x * encCost) if x > 0 else flatCost
            if ln & 1 == 0:
                mid = (l + r) // 2
                res = min(res, dfs(l, mid) + dfs(mid + 1, r))
            return res

        return dfs(0, n - 1)