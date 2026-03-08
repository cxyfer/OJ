import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        ans = -1
        for i, c in enumerate(capacity):
            if c >= itemSize and (ans == -1 or c < capacity[ans]):
                ans = i
        return ans