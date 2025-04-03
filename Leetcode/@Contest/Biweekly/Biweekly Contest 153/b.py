import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        ans = 0
        segs = []
        i = 0
        while i < n:
            st = i
            while i < n and s[i] == s[st]:
                i += 1
            if s[st] == '1':
                ans += i - st
            else:
                segs.append(i - st)
        mx = 0
        for x, y in pairwise(segs):
            mx = max(mx, x + y)
        return ans + mx

sol = Solution()
print(sol.maxActiveSectionsAfterTrade("01"))  # 1
print(sol.maxActiveSectionsAfterTrade("0100"))  # 4
print(sol.maxActiveSectionsAfterTrade("1000100"))  # 7
print(sol.maxActiveSectionsAfterTrade("01010"))  # 4