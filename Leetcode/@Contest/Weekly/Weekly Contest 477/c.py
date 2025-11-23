import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

MOD = int(1e9 + 7)

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)

        s1 = [0] * (n + 1)
        s2 = [0] * (n + 1)
        sd = [0] * (n + 1)
        for r, c in enumerate(s, start=1):
            d = int(c)
            s1[r] = s1[r - 1] + d
            s2[r] = ((s2[r - 1] * 10 + d) % MOD) if d > 0 else (s2[r - 1])
            sd[r] = sd[r - 1] + int(d > 0)

        ans = []
        for l, r in queries:
            s = s1[r + 1] - s1[l]
            x = s2[r + 1] - s2[l] * pow(10, sd[r + 1] - sd[l], MOD)
            ans.append(s * x % MOD)
        return ans

sol = Solution()
print(sol.sumAndMultiply("10203004", [[0,7],[1,3],[4,6]]))  # [12340, 4, 9]


"""

10203004

1 1 12 12 123 123 1234
234
1234
"""