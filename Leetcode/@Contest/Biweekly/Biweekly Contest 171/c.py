import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        n = len(technique1)
        arr = [x - y for x, y in zip(technique1, technique2)]
        arr.sort(reverse=True)
        ans = sum(technique2) + sum(arr[:k])
        for i in range(k, n):
            if arr[i] > 0:
                ans += arr[i]
        return ans