import math
from typing import *
from collections import *
from functools import lru_cache, cache
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        cnt = Counter()
        for i in range(0, n, k):
            cnt[word[i:i+k]] += 1
        ans = n // k - max(cnt.values())
        return ans
sol = Solution()
print(sol.minimumOperationsToMakeKPeriodic("leetcodeleet", 4)) # 1