import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def minimumLength(self, s: str) -> int:
        pos = [[] for _ in range(26)]
        for i, ch in enumerate(s):
            pos[ord(ch) - ord('a')].append(i)
        for i, ch in enumerate(s):
            if len(pos[ord(ch) - ord('a')]) >= 3:
                pos[ord(ch) - ord('a')].pop(2)
                pos[ord(ch) - ord('a')].pop(0)
        return sum(len(pos[i]) for i in range(26))

sol = Solution()
print(sol.minimumLength("abaacbcbb")) # 5
print(sol.minimumLength("aa")) # 2
