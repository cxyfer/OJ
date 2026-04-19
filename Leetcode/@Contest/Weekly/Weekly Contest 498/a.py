import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        mx = float('-inf')
        suf = list(accumulate(nums[::-1], func=min))[::-1]
        for i, x in enumerate(nums):
            mx = max(mx, x)
            if (mx - suf[i]) <= k:
                return i
        return -1