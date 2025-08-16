import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        sz = (2 * k + 1)
        return math.ceil(n / sz) * math.ceil(m / sz)