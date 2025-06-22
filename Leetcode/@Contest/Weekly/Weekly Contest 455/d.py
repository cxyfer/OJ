import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from math import *

class Solution:
    def minTime(self, n: int, k: int, m: int, time: List[int], mul: List[float]) -> float:
        if k == 1 and n > 1:
            return -1
        U = (1 << n) - 1
        hp = [(0, 0, 0)]  # (t, mask, stage)
        dist = [[float("inf")] * m for _ in range(1 << n)]
        dist[0][0] = 0
        while hp:
            t, msk, st = heappop(hp)
            if msk == U:
                return t
            if t > dist[msk][st]:
                continue
            idxs = [i for i in range(n) if not ((msk >> i) & 1)]
            for sz in range(1, min(k, len(idxs)) + 1):
                for g in combinations(idxs, sz):
                    mx = max(time[i] for i in g)
                    d1 = mx * mul[st]
                    nst1 = (st + math.floor(d1)) % m
                    nmsk = msk
                    for idx in g:
                        nmsk |= (1 << idx)
                    if nmsk != U:
                        dsts = [i for i in range(n) if ((nmsk >> i) & 1)]
                        for idx in dsts:
                            d2 = time[idx] * mul[nst1]
                            nt = t + d1 + d2
                            nst2 = (nst1 + math.floor(d2)) % m
                            if nt < dist[nmsk ^ (1 << idx)][nst2]:
                                dist[nmsk ^ (1 << idx)][nst2] = nt
                                heappush(hp, (nt, nmsk ^ (1 << idx), nst2))
                    else:
                        nt = t + d1
                        if nt < dist[nmsk][nst1]:
                            dist[nmsk][nst1] = nt
                            heappush(hp, (nt, nmsk, nst1))
        return -1
    
sol = Solution()
print(sol.minTime(1, 1, 2, [5], [1.0,1.3])) # 5.00000
print(sol.minTime(3, 2, 3, [2,5,8], [1.0,1.5,0.75])) # 14.50000
print(sol.minTime(2, 3, 4, [40,1], [1.82,1.59,1.11,1.84])) # 47.81000
print(sol.minTime(3, 2, 4, [68,26,46], [0.82,1.46,1.55,1.93])) # 160.64000
print(sol.minTime(3, 2, 5, [6,23,98], [1.86,1.3,0.67,1.48,0.71])) # 123.85000
print(sol.minTime(4, 5, 4, [37,100,71,5], [1.14,0.53,0.55,0.97])) # 100.00000