import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        v = list(map(lambda x : x * x, nums))
        v.sort()
        return sum(v[n//2:]) - sum(v[:n//2])