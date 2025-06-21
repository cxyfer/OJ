import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = [0, 0]
        for x in nums:
            cnt[x & 1] += 1
        if abs(cnt[0] - cnt[1]) > 1:
            return -1
        def cal(b):
            src = [i for i, x in enumerate(nums) if x & 1 == 0]
            tgt = [i for i in range(n) if i & 1 == b]
            return sum(abs(x - y) for x, y in zip(src, tgt)) if len(src) == len(tgt) else float("inf")
        return min(cal(0), cal(1))