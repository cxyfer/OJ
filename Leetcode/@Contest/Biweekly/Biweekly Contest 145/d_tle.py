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

N = int(math.isqrt(int(1e9))) + 1
is_prime = [True] * N
is_prime[0] = is_prime[1] = False
for i in range(2, int(math.sqrt(N)) + 1):
    if is_prime[i]:
        for j in range(i * i, N, i):
            is_prime[j] = False
primes = [i for i in range(N) if is_prime[i]]

class Solution:
    def countComponents(self, nums, threshold):
        S1 = [x for x in nums if x <= threshold]
        S2 = [x for x in nums if x > threshold]
        if not S1:
            return len(S2)
        S1.sort()
        n = len(S1)

        factors = defaultdict(list)
        for i, x in enumerate(S1):
            facs = []
            curr = x
            for p in primes:
                if p * p > curr:
                    break
                if curr % p == 0:
                    facs.append(p)
                    while curr % p == 0:
                        curr //= p
            if curr > 1:
                facs.append(curr)
            for f in facs:
                factors[f].append(i)

        uf = UnionFind(n)
        for p, lst in factors.items():
            lst.sort(key=lambda idx: S1[idx])
            hub = lst[0]
            hub_val = S1[hub]
            for i in range(1, len(lst)):
                x, y = lst[i-1], lst[i]
                a, b = S1[x], S1[y]
                if math.lcm(a, b) <= threshold:
                    uf.union(x, y)
                if math.lcm(hub_val, b) <= threshold:
                    uf.union(hub, y)
        for i in range(len(S1) - 1):
            a, b = S1[i], S1[i+1]
            if math.lcm(a, b) <= threshold:
                uf.union(i, i+1)
            if math.lcm(S1[0], b) <= threshold:
                uf.union(0, i+1)
        return uf.cnt + len(S2)

sol = Solution()
print(sol.countComponents([2,4,8,3,9], 5)) # 4
print(sol.countComponents([2,4,8,3,9,12], 10)) # 2
print(sol.countComponents([31,33,11], 90)) # 2
print(sol.countComponents([41,1,20], 80)) # 1
print(sol.countComponents([18,57,98,81], 170)) # 3
print(sol.countComponents([91,39,2,70], 194)) # 1
print(sol.countComponents([53,75,25,20], 183)) # 2
print(sol.countComponents([69,52,99,12,18,119], 240)) # 3

[69,52,99,12,18,119]
240