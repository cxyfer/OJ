import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set('aeiou')
        cnt1, cnt2 = defaultdict(int), defaultdict(int)
        for c in s:
            if c in vowels:
                cnt1[c] += 1
            else:
                cnt2[c] += 1
        return (max(cnt1.values()) if cnt1 else 0) + (max(cnt2.values()) if cnt2 else 0)

sol = Solution()
print(sol.maxFreqSum("successes")) # 6
print(sol.maxFreqSum("aeiaeia")) # 3
