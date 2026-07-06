import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *


class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        # return 0 if (d1 := abs(x - z)) == (d2 := abs(y - z)) else (1 if d1 < d2 else 2)
        d1 = abs(x - z)
        d2 = abs(y - z)
        return ((d1 > d2) << 1) | (d1 < d2)
