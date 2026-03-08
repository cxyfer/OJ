import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        t = "".join(sorted(s))

        if s == t:
            return 0
        if n == 2 and s != t:
            return -1

        cnt = Counter(s)
        mn, mx = min(s), max(s)
        if s[0] == mn or s[-1] == mx:
            return 1
        if s[0] == mx and s[-1] == mn and cnt[mx] == 1 and cnt[mn] == 1:
            return 3
        return 2