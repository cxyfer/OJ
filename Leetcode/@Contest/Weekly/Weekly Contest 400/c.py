import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)
        cnt = [0] * 26
        pos = [[] for _ in range(26)]
        for i, ch in enumerate(s):
            idx = ord(ch) - ord("a")
            if ch != "*":
                pos[idx].append(i)
                cnt[idx] += 1
            else:
                for i in range(26):
                    if cnt[i] > 0:
                        cnt[i] -= 1
                        pos[i].pop()
                        break
        lst = []
        for i in range(26):
            lst.extend(pos[i])
        lst.sort()
        ans = "".join(s[i] for i in lst)
        return ans

sol = Solution()

"aaba*"
"abc"
print(sol.clearStars("aaba*")) # "aaab"
print(sol.clearStars("abc")) # "abc"