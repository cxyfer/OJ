import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        ans = 0
        prev = float('inf')
        for h in maximumHeight:
            cur = min(h, prev - 1)
            if cur < 1:
                return -1
            ans += cur
            prev = cur
        return ans

