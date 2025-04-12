import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n
        return 1 << n.bit_length()
    
def calc(n):
    st = set()
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                st.add(i ^ j ^ k)
    return len(st)

sol = Solution()
for n in range(1, 100):
    # print(n, calc(n))
    assert calc(n) == sol.uniqueXorTriplets(list(range(1, n + 1)))
