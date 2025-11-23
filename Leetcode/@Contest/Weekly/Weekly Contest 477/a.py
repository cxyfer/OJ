import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = [d for d in str(n) if int(d) > 0]
        if not x:
            x = ['0']
        s = sum([int(d) for d in x])
        return int(''.join(x)) * s