import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *


class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        b = 0
        ans = [0, 0]
        for i, x in enumerate(nums, 1):
            if x & 1:
                b ^= 1
            if i % 6 == 0:
                b ^= 1
            ans[b] += x
        return ans[0] - ans[1]
