import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def minimumChairs(self, s: str) -> int:
        ans = cur = 0
        for ch in s:
            if ch == 'E':
                cur += 1
                ans = max(ans, cur)
            else:
                cur -= 1
        return ans