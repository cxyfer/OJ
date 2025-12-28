import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def countBalanced(self, low: int, high: int) -> int:
        diff = len(str(high)) - len(str(low))
        high = list(map(int, str(high)))
        n = len(high)
        low = list(map(int, str(low).zfill(n)))  # 補前導零，使 low 和 high 對齊

        @cache
        def dfs(i: int, s: int, flag: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return 1 if s == 0 else 0

            # 第 i 個數位可以從 lo 枚舉到 hi
            # 如果對數位還有其它約束，應該只在下面的 for 迴圈做限制，不應修改 lo 或 hi
            lo = low[i] if limit_low else 0
            hi = high[i] if limit_high else 9

            res = 0
            if i < diff and limit_low:
                res += dfs(i + 1, 0, 0, True, False)  # 前導 0
            for d in range(1 if i < diff and limit_low else lo, hi + 1):
                res += dfs(i + 1, s + (d if flag == 0 else -d), flag ^ 1, limit_low and d == lo, limit_high and d == hi)
            return res

        return dfs(0, 0, 0, True, True)

sol = Solution()
print(sol.countBalanced(1, 100))  # 9