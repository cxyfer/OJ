import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v = sum(ch in "aeiou" for ch in s)
        c = sum(ch.isalpha() and ch not in "aeiou" for ch in s)
        return math.floor(v / c) if c > 0 else 0