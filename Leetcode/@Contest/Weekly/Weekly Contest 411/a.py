import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        def check(s):
            cnt0 = cnt1 = 0
            for ch in s:
                if ch == "0":
                    cnt0 += 1
                else:
                    cnt1 += 1
            return cnt0 <= k or cnt1 <= k
        ans = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                if check(s[i:j]):
                    ans += 1
        return ans
    
sol = Solution()
print(sol.countKConstraintSubstrings("10101", 1)) # 12
