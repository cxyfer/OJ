import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        n = len(numWays)
        ans = []
        f = [1] + [0] * n
        for i, w in enumerate(numWays, 1):
            if w - f[i] == 1:
                ans.append(i)
                for j in range(i, n + 1):
                    f[j] += f[j - i]
            elif w - f[i] != 0:
                return []
        return ans

sol = Solution()
print(sol.findCoins([0,1,0,2,0,3,0,4,0,5])) # [2,4,6]
print(sol.findCoins([1,2,2,3,4])) # [1,2,5]