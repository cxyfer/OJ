import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def minimumFlips(self, n: int) -> int:
        s = bin(n)[2:]
        return sum(a != b for a, b in zip(s, reversed(s)))