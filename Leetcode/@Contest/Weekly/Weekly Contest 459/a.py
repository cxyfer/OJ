import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = [d for d in map(int, str(n))]
        s = sum(digits) + reduce(mul, digits, 1)
        return (n % s) == 0