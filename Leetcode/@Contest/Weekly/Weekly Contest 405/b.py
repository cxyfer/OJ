import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        def dfs(i, s):
            if i == n:
                res = bin(s)[2:].zfill(n)
                if not any(x == y == "0" for x, y in pairwise(res)):
                    ans.append(res)
                return
            dfs(i + 1, s << 1)
            dfs(i + 1, s << 1 | 1)
        dfs(0, 0)
        return ans
    
sol = Solution()
print(sol.validStrings(3)) # ["010","011","101","110","111"]
print(sol.validStrings(1)) # ["0","1"]