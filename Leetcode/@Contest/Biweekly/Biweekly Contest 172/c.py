import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
腦筋急轉彎
注意到 1 只能往左交換，所以只能在以左的位置選一個放
維護 MaxHeap，每次遇到 1 就 pop 出最大的元素，累加答案
"""

class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        ans = 0
        hp = []
        for x, ch in zip(nums, s):
            heappush(hp, -x)
            if ch == '1':
                y = -heappop(hp)
                ans += y
        return ans