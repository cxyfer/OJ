import math
from typing import *
from collections import *
from functools import lru_cache, cache
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def minAnagramLength(self, s: str) -> int:
        return self.solve1(s)
    def solve1(self, s: str) -> int:
        n = len(s)
        cnt = [0] * 26
        for k in range(1, n+1): # 枚舉可能的長度
            cnt[ord(s[k-1]) - ord("a")] += 1
            if n % k != 0: continue
            flag = True
            for i in range(k, n, k):
                cnt2 = [0] * 26
                for j in range(k):
                    cnt2[ord(s[i+j]) - ord("a")] += 1
                if cnt2 != cnt:
                    flag = False
                    break
            if flag:
                return k
        return n
sol = Solution()
print(sol.minAnagramLength("abba")) # 2
print(sol.minAnagramLength("cdef")) # 4
print(sol.minAnagramLength("oionssonoi")) # 5

