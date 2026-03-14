import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        cnt = Counter(nums)
        for x in nums:
            if cnt[x] == 1 and x & 1 == 0:
                return x
        return -1