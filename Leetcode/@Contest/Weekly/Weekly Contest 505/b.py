import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
Q2: 二進制枚舉
注意到 n <= 12，因此可以考慮枚舉 [0, 2^n) 對應的二進制字串。
可以先檢查是否有連續的 1，這部分和昨天的 Q1 有些類似，然後計算成本。
"""

class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        ans = []
        for s in range(1 << n):
            if (s & (s >> 1)) > 0:
                continue
            cost = 0
            t = s
            while t:
                lb = t & (-t)
                b = lb.bit_length() - 1
                cost += n - b - 1
                t ^= lb
            if cost <= k:
                ans.append(f"{s:0{n}b}")
        return ans
