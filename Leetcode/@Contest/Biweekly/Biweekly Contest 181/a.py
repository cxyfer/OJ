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
        n = str(n)
        x = str(x)
        return (x in n) and not n.startswith(x)