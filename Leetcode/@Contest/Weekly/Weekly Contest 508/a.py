import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *


class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        ans = 0
        for x in nlargest(k, nums):
            if mul > 1:
                ans += x * mul
                mul -= 1
            else:
                ans += x
        return ans