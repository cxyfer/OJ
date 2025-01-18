import math
from typing import *
from collections import *
from functools import lru_cache, cache
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        cnt = defaultdict(Counter)
        for x in nums:
            d = 0
            while x:
                cnt[d][x % 10] += 1
                x //= 10
                d += 1
        # print(cnt)
        ans = 0
        for d in cnt:
            tol = sum(cnt[d].values())
            cur = 0
            for k, v in cnt[d].items():
                cur += (tol - v) * v
            ans += cur // 2
            # print(d, ans)
        return ans

sol = Solution()
# print(sol.sumDigitDifferences([13,23,12])) # 4
# print(sol.sumDigitDifferences([10,10,10,10])) # 0


print(sol.sumDigitDifferences([824,843,837,620,836,234,276,859])) # 67