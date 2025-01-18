import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class UnionFind:
    def __init__(self, n):
        self.pa = list(range(n))
        self.sz = [1] * n
        self.cnt = n

    def find(self, x):
        while self.pa[x] != x:
            self.pa[x] = self.pa[self.pa[x]]
            x = self.pa[x]
        return x

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.sz[px] < self.sz[py]:
            px, py = py, px
        self.pa[py] = px
        self.sz[px] += self.sz[py]
        self.cnt -= 1
        return True

N = (int(2e5) + 10)
factors = [[] for _ in range(N)]
for i in range(1, N):
    for j in range(i, N, i):
        factors[j].append(i)

class Solution:
    def countComponents(self, nums, threshold):
        n = len(nums)
        nums.sort()
        facs = [[] for _ in range(threshold + 1)]
        for i, x in enumerate(nums):
            if x > threshold:
                continue
            for f in factors[x]:
                if f > threshold:
                    break
                facs[f].append(i)

        uf = UnionFind(n)
        for g in range(1, threshold + 1):
            if not facs[g]:
                continue
            limit = threshold * g
            for i in range(1, len(facs[g])):
                x, y = facs[g][0], facs[g][i]
                if nums[x] * nums[y] <= limit:
                    uf.union(x, y)
        return uf.cnt
    
sol = Solution()
print(sol.countComponents([2,4,8,3,9], 5)) # 4
print(sol.countComponents([2,4,8,3,9,12], 10)) # 2
print(sol.countComponents([31,33,11], 90)) # 2
print(sol.countComponents([41,1,20], 80)) # 1
print(sol.countComponents([18,57,98,81], 170)) # 3
print(sol.countComponents([91,39,2,70], 194)) # 1
print(sol.countComponents([53,75,25,20], 183)) # 2
print(sol.countComponents([69,52,99,12,18,119], 240)) # 3