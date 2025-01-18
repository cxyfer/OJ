import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    """
        Similar to 56. Merge Intervals
    """
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        intervals = []
        meetings.sort(key=lambda x: x[0])
        for x, y in meetings:
            if not intervals or x > intervals[-1][1]:
                intervals.append([x, y])
            else:
                intervals[-1][1] = max(intervals[-1][1], y) 
        ans = days
        for x, y in intervals:
            ans -= y - x + 1
        return ans