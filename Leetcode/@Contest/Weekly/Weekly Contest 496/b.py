import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

MAX_N = int(1e9)
cnt = defaultdict(int)
for a in count(1):
    if a ** 3 > MAX_N:
        break
    for b in count(a):
        x = a ** 3 + b ** 3
        if x > MAX_N:
            break
        cnt[x] += 1
A = sorted(x for x, v in cnt.items() if v >= 2)

class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        return A[:bisect_right(A, n)]