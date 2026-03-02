import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        cnt = Counter(nums)
        x = min(cnt.keys())
        for y in sorted(cnt.keys()):
            if cnt[x] != cnt[y]:
                return [x, y]
        return [-1, -1]