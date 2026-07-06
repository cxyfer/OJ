import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

MOD = int(1e9) + 7
class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        def convert(n):
            if n == 0:
                return "0"
            res = ""
            while n > 0:
                res += str(n % b)
                n //= b
            return res[::-1]

        high = list(map(int, convert(int(r))))
        n = len(high)
        low = list(map(int, convert(int(l)).zfill(n)))  # 補前導零，使 low 和 high 對齊

        @cache
        def dfs(i: int, pre: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return 1

            # 第 i 個數位可以從 lo 枚舉到 hi
            # 如果對數位還有其它約束，應該只在下面的 for 迴圈做限制，不應修改 lo 或 hi
            lo = low[i] if limit_low else 0
            hi = high[i] if limit_high else b - 1
            res = 0
            for d in range(max(lo, pre), hi + 1):
                res = (res + dfs(i + 1, d, limit_low and d == lo, limit_high and d == hi)) % MOD
            return res

        return dfs(0, 0, True, True)

sol = Solution()
print(sol.countNumbers("23", "28", 8))  # 3
print(sol.countNumbers("2", "7", 2))  # 2

l = "94466559861923903056101755850610116867850282195"
r = "6404483317788505367977730467756261386503597091682039038723558"
b = 8
print(sol.countNumbers(l, r, b))  # 628660062