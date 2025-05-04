import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def maxProduct(self, n: int) -> int:
        digits = map(int, str(n))
        ans = mx = 0
        for d in digits:
            ans = max(ans, mx * d)
            mx = max(mx, d)
        return ans

sol = Solution()
print(sol.maxProduct(273))  # 72
print(sol.maxProduct(749))  # 84
