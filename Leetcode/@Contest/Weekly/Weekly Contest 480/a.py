import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        # return sum(nlargest(k, nums)) - sum(nsmallest(k, nums))
        nums.sort()
        return sum(nums[-k:]) - sum(nums[:k])