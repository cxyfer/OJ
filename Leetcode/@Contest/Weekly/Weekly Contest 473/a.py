import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def removeZeros(self, n: int) -> int:
        return int(str(n).replace('0', ''))