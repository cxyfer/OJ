import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        n = len(nums)
        i = 0
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        s1 = sum(nums[:i + 1])
        s2 = sum(nums[i:])
        if s1 > s2:
            return 0
        elif s2 > s1:
            return 1
        else:
            return -1