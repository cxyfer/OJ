import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *


class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        n, x = str(n), str(x)
        return (x in n) and not n.startswith(x)
        # ok = False
        # while n >= 10:
        #     n, r = divmod(n, 10)
        #     ok |= (r == x)
        # return ok and n != x