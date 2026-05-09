import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
Q1: ||模擬|| 
直接根據題意模擬即可。
"""

class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        ans = cnt = 0
        for s in events:
            if s.isdigit():
                ans += int(s)
            elif s == "W":
                cnt += 1
            else:
                ans += 1
            if cnt == 10:
                break
        return [ans, cnt]