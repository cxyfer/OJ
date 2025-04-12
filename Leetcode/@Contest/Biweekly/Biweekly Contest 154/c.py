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

        st = set([nums[0]])
        pre = set([0])  # nums[i] ^ nums[j]

        for k in range(1, n):
            for i in range(k + 1):
                pre.add(nums[i] ^ nums[k])  # nums[i] ^ nums[j]
            for p in pre:
                st.add(p ^ nums[k])  # (nums[i] ^ nums[j]) ^ nums[k]
        return len(st)
    
sol = Solution()
print(sol.uniqueXorTriplets([1,3])) # 2
print(sol.uniqueXorTriplets([6,7,8,9])) # 4

st = set()
for i in range(1, 1501):
    for j in range(1, 1501):
        st.add(i ^ j)
print(min(st), max(st))