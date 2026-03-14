import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        cnt = cnt1 + cnt2

        ans = 0
        for k in cnt.keys():
            d = abs(cnt1[k] - cnt2[k])
            if d & 1:
                return -1
            ans += d // 2
        return ans // 2