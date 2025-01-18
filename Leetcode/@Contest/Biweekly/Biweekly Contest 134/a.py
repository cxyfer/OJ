import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        ans = 0
        for i in range(n):
            a, b, c = colors[(i-1) % n], colors[i], colors[(i+1) % n]
            if a != b and b != c:
                ans += 1
        return ans