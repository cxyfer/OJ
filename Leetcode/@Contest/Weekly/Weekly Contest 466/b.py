import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def minOperations(self, s: str) -> int:
        return max((ord('a') - ord(ch)) % 26 for ch in s)

sol = Solution()
print(sol.minOperations("yz"))  # 2