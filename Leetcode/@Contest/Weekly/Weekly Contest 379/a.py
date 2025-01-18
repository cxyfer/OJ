import math
from typing import *
from collections import *
from functools import lru_cache, cache
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_d = float("-inf")
        ans = float("-inf")
        cnt = defaultdict(int)
        for x, y in dimensions:
            d = math.sqrt(x * x + y * y)
            cnt[d] = max(cnt[d], x * y)
            if d > max_d:
                max_d = d
                ans = cnt[d]
        return cnt[max(cnt.keys())]