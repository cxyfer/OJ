import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if any(x < k for x in nums):
            return -1
        
        if all(x == k for x in nums):
            return 0
        
        return sum(1 for v in set(nums) if v > k)