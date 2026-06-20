import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
Q4: 數位DP
這種在 [l, r] 區間內計數的問題，通常可以使用數位DP來解決。
本題只須要維護前一個數位的值 pre，並且讓當前數位的值 d 與 pre 的差值不大於 k 就行了，
注意當還沒有填數字的時候應該要設置成 0~9 以外的值，並特判此種情況，以免誤對第一個數位造成限制。
"""

class Solution:
    def goodIntegers(self, l: int, r: int, k: int) -> int:
        n = len(str(r))
        diff = n - len(str(l))
        high = list(map(int, str(r)))
        low = list(map(int, str(l).zfill(n)))

        @cache
        def dfs(i: int, pre: int, limit_low: bool, limit_high: bool):
            if i == n:
                return 1

            lo = low[i] if limit_low else 0
            hi = high[i] if limit_high else 9

            res = 0
            if i < diff and limit_low:
                res += dfs(i + 1, -1, True, False)
            for d in range(1 if i < diff and limit_low else lo, hi + 1):
                if pre == -1 or abs(pre - d) <= k:
                    res += dfs(i + 1, d, limit_low and d == lo, limit_high and d == hi)
            return res

        ans = dfs(0, -1, True, True)
        dfs.cache_clear()
        return ans

sol = Solution()
print(sol.goodIntegers(10, 15, 1))  # 3