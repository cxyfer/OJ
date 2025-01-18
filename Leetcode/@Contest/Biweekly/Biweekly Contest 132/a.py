import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def clearDigits(self, s: str) -> str:
        n = len(s)
        ans = [""] * n
        pos = []
        for i in range(n):
            if s[i].isdigit():
                ans[i] = ""
                ans[pos[-1]] = ""
                pos.pop()
            else:
                pos.append(i)
                ans[i] = s[i]
        return "".join(ans)

sol = Solution()
print(sol.clearDigits("ab123")) # "ab"