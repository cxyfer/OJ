import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *
from math import inf

"""
Q4: 劃分型DP

令 f[i] 表示使 source[i:] 變成 target[i:] 的最小代價，
則可以枚舉每條 rule 是否匹配，並轉移到 f[i + len(pattern)]
"""


class Solution:
    def minCost(self, source: str, target: str, rules: list[list[str]], costs: list[int]) -> int:
        n = len(source)

        @cache
        def dfs(i: int) -> int:
            if i == n:
                return 0

            res = inf
            if source[i] == target[i]:
                res = dfs(i + 1)
            for (pattern, replacement), cost in zip(rules, costs):
                m = len(pattern)
                if i + m > n:
                    continue
                ok = True
                for j, ch in enumerate(pattern):
                    if ch != "*" and ch != source[i + j]:
                        ok = False
                        break
                for j, ch in enumerate(replacement):
                    if ch != target[i + j]:
                        ok = False
                        break
                if not ok:
                    continue
                res = min(res, cost + pattern.count("*") + dfs(i + m))
            return res

        ans = dfs(0)
        dfs.cache_clear()
        return ans if ans != inf else -1
