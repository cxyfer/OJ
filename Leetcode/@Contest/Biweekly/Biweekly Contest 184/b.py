import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
## Q2: 合併區間 + 貪心

對於某個需要亮燈時間點，需要點幾盞燈是可以貪心決定的，由於一個燈可以點亮三個位置，因此需要點的燈數就是 ceil(brightness / 3)。
而不同時間點的計算方式是相同的，因此我們只需要知道區間長度即可，由於題目沒有保證區間互斥，因此需要先合併區間。
"""


class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        # 56. Merge Intervals
        intervals.sort()
        merged = []
        for l, r in intervals:
            if not merged or l > merged[-1][1]:
                merged.append([l, r])
            else:
                merged[-1][1] = max(merged[-1][1], r)

        k = (brightness + 3 - 1) // 3
        ans = 0
        for l, r in merged:
            ans += k * (r - l + 1)
        return ans
