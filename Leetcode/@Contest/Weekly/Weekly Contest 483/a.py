import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def largestEven(self, s: str) -> str:
        s = list(s)
        while s and int(s[-1]) & 1:
            s.pop()
        return ''.join(s)