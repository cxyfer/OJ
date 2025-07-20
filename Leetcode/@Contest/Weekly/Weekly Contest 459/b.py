import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from math import comb

MOD = int(1e9 + 7)
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        cnt = defaultdict(int)
        for x, y in points:
            cnt[y] += 1

        ans = s = 0
        for y, v in cnt.items():
            if v >= 2:
                ans += comb(v, 2) * s
                s += comb(v, 2)
        return ans % MOD