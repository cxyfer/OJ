import math
from re import S
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def countDistinct(self, n: int) -> int:
        s = str(n)
        m = len(s)

        # 9 + 9^2 + ... + 9^(m-1) = (9^m - 9) / 8
        p = 9 ** m
        ans = (p - 9) // 8 
 
        for i, c in enumerate(s):
            d = int(c)
            if d == 0:
                break
            p //= 9
            ans += (d - 1) * p
        else:
            ans += 1

        return ans

sol = Solution()
print(sol.countDistinct(10))
print(sol.countDistinct(3))