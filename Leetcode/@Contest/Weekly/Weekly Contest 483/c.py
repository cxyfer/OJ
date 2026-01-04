import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def minimumCost(self, s: str, t: str, flipCost: int, swapCost: int, crossCost: int) -> int:
        cnt = [0] * 4
        for a, b in zip(s, t):
            cnt[(ord(a) - ord('0')) << 1 | (ord(b) - ord('0'))] += 1
        ans = 0
        ans += min(cnt[1], cnt[2]) * min(swapCost, flipCost << 1)
        ans += abs(cnt[1] - cnt[2]) // 2 * min(crossCost + swapCost, flipCost << 1)
        if abs(cnt[1] - cnt[2]) & 1:
            ans += flipCost
        return ans


sol = Solution()
print(sol.minimumCost("01000", "10111", 10, 2, 2))  # 16
print(sol.minimumCost("001", "110", 2, 100, 100))  # 6
print(sol.minimumCost("1010", "1010", 5, 5, 5))  # 0