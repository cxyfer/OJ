import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        high = list(map(int, str(num2)))
        n = len(high)
        low = list(map(int, str(num1)))  # 補前導零，使 low 和 high 對齊
        diff = n - len(low)
        low = [0] * diff + low
        assert len(low) == len(high)

        @cache
        def dfs(i: int, p1: int, p2: int, cnt: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return cnt

            # 第 i 個數位可以從 lo 枚舉到 hi
            # 如果對數位還有其它約束，應該只在下面的 for 迴圈做限制，不應修改 lo 或 hi
            lo = low[i] if limit_low else 0
            hi = high[i] if limit_high else 9

            res = 0
            if i < diff and limit_low:
                res += dfs(i + 1, -1, -1, 0, True, False)  # 前導 0
                # assert lo == 0
            for d in range(1 if i < diff and limit_low else lo, hi + 1):
                res += dfs(i + 1, p2, d, cnt + int(p1 != -1 and p2 != -1 and (p1 < p2 > d) or (p1 > p2 < d)), limit_low and d ==
                           lo, limit_high and d == hi)
            return res

        return dfs(0, -1, -1, 0, True, True)