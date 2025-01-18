import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        n = len(word)
        MOD = 10**9 + 7

        groups = []
        i = 0
        while i < n:
            j = i
            while j < n and word[j] == word[i]:
                j += 1
            groups.append(j - i)
            i = j

        m = len(groups)
        need = k - m
        if k > sum(groups):
            return 0

        tot = 1
        for ln in groups:
            tot = (tot * ln) % MOD

        if m >= k or need <= 0:
            return tot

        f = [0] * (need)
        f[0] = 1
        for ln in groups:
            max_add = ln - 1
            if max_add <= 0:
                continue

            pre = [0] * (need)
            pre[0] = f[0]
            for s in range(1, need):
                pre[s] = (pre[s - 1] + f[s]) % MOD

            new_f = [0] * (need)
            for s in range(need):
                lower = max(0, s - max_add)
                new_f[s] = pre[s]
                if lower > 0:
                    new_f[s] = (new_f[s] - pre[lower - 1]) % MOD

            f = new_f

        return (tot - sum(f) % MOD) % MOD


sol = Solution()
print(sol.possibleStringCount("aabbccdd", 7)) # 5
print(sol.possibleStringCount("aabbccdd", 8)) # 1
print(sol.possibleStringCount("aaabbb", 3)) # 8
print(sol.possibleStringCount("d", 1)) # 1


sol.possibleStringCount("d", 1) 