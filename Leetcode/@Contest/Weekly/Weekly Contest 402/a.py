import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        ans = 0
        cnt = defaultdict(int)
        for x in hours:
            if x % 24 == 0:
                ans += cnt[0]
            ans += cnt[24 - (x % 24)]
            cnt[x % 24] += 1
        return ans
    
sol = Solution()
print(sol.countCompleteDayPairs([12,12,30,24,24])) # 2
print(sol.countCompleteDayPairs([72,48,24,3])) # 3