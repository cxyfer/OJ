import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        return all(abs(a - b) <= 2 for a, b in pairwise(map(int, s)))