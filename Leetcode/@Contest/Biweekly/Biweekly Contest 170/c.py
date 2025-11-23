import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:
        m = n * (n + 1) // 2
        if target > m or target < -m or (d := m - target) & 1:
            return []
        ans = list(range(n, 0, -1))
        for i, x in enumerate(ans):
            if 2 * x <= d:
                d -= 2 * x
                ans[i] = -x
        ans.sort()
        return ans

sol = Solution()
print(sol.lexSmallestNegatedPerm(3, 0))  # [-3,1,2]