import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        ans = 0
        i = 0
        while i < n:
            j = i
            while j < n and word[j] == word[i]:
                j += 1
            ans += j - i - 1
            i = j
        return ans + 1


sol = Solution()
print(sol.possibleStringCount("abbcccc")) # 5
print(sol.possibleStringCount("abcd")) # 1
print(sol.possibleStringCount("aaaa")) # 4
