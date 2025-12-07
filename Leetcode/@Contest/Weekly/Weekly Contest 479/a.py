import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        nums.sort(key = lambda x : (int(bin(x)[2:][::-1], 2), x))
        return nums