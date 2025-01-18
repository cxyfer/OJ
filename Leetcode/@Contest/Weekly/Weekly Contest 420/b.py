import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            cnt = defaultdict(int)
            mx = 0
            for j in range(i, n):
                ch = s[j]
                cnt[ch] += 1
                mx = max(mx, cnt[ch])
                if mx >= k:
                    ans += 1
        return ans

sol = Solution()
print(sol.numberOfSubstrings("abacb", 2)) # 4
print(sol.numberOfSubstrings("abcde", 1)) # 15
print(sol.numberOfSubstrings("aaabb", 3)) # 3