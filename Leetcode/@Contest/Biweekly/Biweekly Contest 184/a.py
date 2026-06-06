import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
## Q1: 閱讀理解

看到 exactly one pair of consecutive set bits 時雖然覺得用 pair 很奇怪，
但因為 consecutive 我以為是分組後恰好有 1 組 1，結果 WA 了一次。
媽的相鄰就寫 adjacent 好嗎？
"""


class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        cnt = 0
        for a, b in pairwise(bin(n)[2:]):
            if a == b == "1":
                cnt += 1
        return cnt == 1
