import math
from math import *
from typing import *
from collections import *
from functools import lru_cache
import heapq
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        res1 = sum([1 for x in nums1 if x in cnt2])
        res2 = sum([1 for x in nums2 if x in cnt1])
        return [res1, res2]
