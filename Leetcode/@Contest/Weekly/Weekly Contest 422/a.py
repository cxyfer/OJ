import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def isBalanced(self, num: str) -> bool:
        s1 = s2 = 0
        for idx, d in enumerate(num):
            if idx % 2 == 0:
                s1 += ord(d) - ord('0')
            else:
                s2 += ord(d) - ord('0')
        return s1 == s2

sol = Solution()
print(sol.isBalanced("24123")) # True
