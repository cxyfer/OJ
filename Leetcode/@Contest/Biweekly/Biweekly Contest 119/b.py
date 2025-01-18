import math
from math import *
from typing import *
from collections import *
from functools import lru_cache
import heapq
from heapq import *
from bisect import *
from itertools import *


class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        ans = 0
        i = 0
        while i < n:
            st = i
            while i + 1 < n and abs(ord(word[i]) - ord(word[i + 1])) <= 1:
                i += 1
            i += 1
            ans += (i - st) // 2
        return ans
    
sol = Solution()
print(sol.removeAlmostEqualCharacters("aaaaa")) # 2
print(sol.removeAlmostEqualCharacters("abddez")) # 2
print(sol.removeAlmostEqualCharacters("zyxyxyz")) # 3