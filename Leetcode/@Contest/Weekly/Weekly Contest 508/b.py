import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *


from typing import List

class Solution:
    def filterOccupiedIntervals(self, intervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:
        intervals.sort()
        merged = []
        for l, r in intervals:
            if not merged or l > merged[-1][1] + 1:
                merged.append([l, r])
            else:
                merged[-1][1] = max(merged[-1][1], r)

        ans = []
        for l, r in merged:
            if r < freeStart or l > freeEnd:
                ans.append([l, r])
            else:
                if l < freeStart:
                    ans.append([l, freeStart - 1])
                if r > freeEnd:
                    ans.append([freeEnd + 1, r])
        return ans

sol = Solution()
print(sol.filterOccupiedIntervals([[2,6],[4,8],[10,10],[10,12],[14,16]], 7, 11))  # Output: [[2,6],[12,12],[14,16]]