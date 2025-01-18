import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = 0
        for x in nums1:
            if x % k != 0: continue
            for y in nums2:
                if x % (y * k) == 0:
                    ans += 1
        return ans