import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

# Note: You are guaranteed that at most 1 index has a negative balance initially.
class Solution:
    def minMoves(self, A: List[int]) -> int:
        n = len(A)
        if sum(A) < 0:
            return -1
        if all(x >= 0 for x in A):
            return 0

        mn = min(A)
        idx = A.index(mn)
        need = -mn
        B = []
        for i, x in enumerate(A):
            if x > 0:
                d = abs(i - idx)
                B.append((min(d, n - d), x))
        B.sort()

        ans = 0
        for d, v in B:
            v = min(need, v)
            ans += v * d
            need -= v
        return ans

sol = Solution()
print(sol.minMoves([5,1,-4]))  # 4