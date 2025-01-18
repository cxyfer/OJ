import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = float('inf')
        for i, x in enumerate(nums):
            y = 0
            while x:
                y += x % 10
                x //= 10
            ans = min(ans, y)
        return ans
