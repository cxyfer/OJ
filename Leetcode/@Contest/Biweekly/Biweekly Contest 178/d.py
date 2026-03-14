import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def countFancy(self, l: int, r: int) -> int:
        diff = len(str(r)) - len(str(l))
        high = list(map(int, str(r)))
        n = len(high)
        low = list(map(int, str(l).zfill(n)))

        def is_good(n: int):
            s = list(map(int, str(n)))
            return all(x < y for x, y in pairwise(s)) or all(x > y for x, y in pairwise(s))

        @cache
        def dfs(i: int, pre: int, s: int, inc: bool, dec: bool,
                limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return 1 if inc or dec or is_good(s) else 0

            # 第 i 個數位可以從 lo 枚舉到 hi
            # 如果對數位還有其它約束，應該只在下面的 for 迴圈做限制，不應修改 lo 或 hi
            lo = low[i] if limit_low else 0
            hi = high[i] if limit_high else 9

            res = 0
            if i < diff and limit_low:
                res += dfs(i + 1, -1, 0, True, True, True, False)  # 前導 0
            for d in range(1 if i < diff and limit_low else lo, hi + 1):
                res += dfs(i + 1, d, s + d,
                           inc and (pre == -1 or d > pre), dec and (pre == -1 or d < pre),
                           limit_low and d == lo, limit_high and d == hi)
            return res
            
        return dfs(0, -1, 0, True, True, True, True)

sol = Solution()
print(sol.countFancy(8, 10))  # 3
print(sol.countFancy(12340, 12341))  # 1
print(sol.countFancy(123456788, 123456788))  # 0