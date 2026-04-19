import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
數位DP

題意：給定7個指定的下標，統計這些被指定的下標上呈現非遞減的16位數有多少個，且這些16位數需要位於 [l, r] 之間。
數位 DP，除了數字的下標外，額外維護上一個指定位填哪個數即可，根據當前位是否為指定的下標判斷該採取哪種策略。
"""

class Solution:
    def countGoodIntegersOnPath(self, l: int, r: int, directions: str) -> int:
        idxs = set([0])
        rr = cc = 0
        for d in directions:
            if d == 'D':
                rr += 1
            else:
                cc += 1
            idxs.add(4 * rr + cc)
        
        n = 16
        high = list(map(int, str(r).zfill(n)))
        low = list(map(int, str(l).zfill(n)))

        @cache
        def dfs(i: int, last: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return 1

            # 第 i 個數位可以從 lo 枚舉到 hi
            # 如果對數位還有其它約束，應該只在下面的 for 迴圈做限制，不應修改 lo 或 hi
            lo = low[i] if limit_low else 0
            hi = high[i] if limit_high else 9

            res = 0
            if i in idxs:
                for d in range(max(lo, last), hi + 1):
                    res += dfs(i + 1, d, limit_low and (d == lo), limit_high and (d == hi))
            else:
                for d in range(lo, hi + 1):
                    res += dfs(i + 1, last, limit_low and (d == lo), limit_high and (d == hi))
            return res
        return dfs(0, -1, True, True)

sol = Solution()
print(sol.countGoodIntegersOnPath(8, 10, "DDDRRR"))  # 2