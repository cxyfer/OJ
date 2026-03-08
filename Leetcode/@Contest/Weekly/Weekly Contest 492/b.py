import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        n = len(nums)
        L, R = sum(nums), 1

        ans = -1
        for i in range(n - 1, -1, -1):
            x = nums[i]
            L -= x
            if R > L:
                break
            if R == L:
                ans = i
            R *= x
        return ans