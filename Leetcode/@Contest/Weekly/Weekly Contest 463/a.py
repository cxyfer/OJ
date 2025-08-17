import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        sp = list(accumulate(prices, initial=0))
        ss = [0] * (n + 1)
        for i, (s, p) in enumerate(zip(strategy, prices), start=1):
            ss[i] = ss[i - 1] + s * p
        ans = ss[n]
        for i in range(k, n + 1):
            origin = ss[n] - ss[i] + ss[i - k]
            # hold = sp[i - k // 2] - sp[i - k]
            sell = sp[i] - sp[i - k // 2]
            ans = max(ans, origin + sell)
        return ans
    
sol = Solution()
print(sol.maxProfit([4,2,8], [-1,0,1], 2))  # 10
print(sol.maxProfit([5,4,3], [1,1,0], 2))  # 9
print(sol.maxProfit([5,8], [-1,-1], 2))  # 8