import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        n = len(order)
        mp = [-1] * (n + 1)
        for i, x in enumerate(order):
            mp[x] = i
        return sorted(friends, key = lambda x : mp[x])