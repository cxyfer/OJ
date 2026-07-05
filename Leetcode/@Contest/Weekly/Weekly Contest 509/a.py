from bisect import *
from collections import *
from functools import *
from heapq import *
from itertools import *
from math import *
from operator import *
from random import *
from string import *
from typing import *


class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        max_d = -1
        ans = 0
        for num in nums:
            lst = list(map(int, str(num)))
            mx, mn = max(lst), min(lst)
            d = mx - mn
            if d > max_d:
                max_d = d
                ans = num
            elif d == max_d:
                ans += num
        return ans
