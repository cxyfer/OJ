import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        ans = []
        suf = list(accumulate(nums[::-1], func=max, initial=float('-inf')))[::-1]
        pre = float('-inf')
        for i, x in enumerate(nums):
            if x > pre or x > suf[i + 1]:
                ans.append(x)
            pre = max(pre, x)
        return ans