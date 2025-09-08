import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return int(any(x != nums[0] for x in nums))