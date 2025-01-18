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

        @cache
        def dp(i, s):
            if s < 0:
                return 0
            if i == m:
                if s >= 0:
                    return 1
                else:
                    return 0
            res = 0
            for x in range(0, min(groups[i] - 1, s) + 1):
                res = (res + dp(i + 1, s - x)) % MOD
            return res
        return (tot - dp(0, need - 1)) % MOD

sol = Solution()
print(sol.possibleStringCount("aabbccdd", 7)) # 5
print(sol.possibleStringCount("aabbccdd", 8)) # 1
print(sol.possibleStringCount("aaabbb", 3)) # 8
print(sol.possibleStringCount("d", 1)) # 1