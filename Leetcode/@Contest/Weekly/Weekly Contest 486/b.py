import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        A = [x for x in nums if x >= 0]
        if (m := len(A)) == 0:
            return nums
        A = A[k % m:] + A[:k % m]
        j = 0
        for i, x in enumerate(nums):
            if x >= 0:
                nums[i] = A[j]
                j += 1
        return nums