import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

N = int(1e4 + 5)
is_prime = [True] * N
is_prime[0] = is_prime[1] = False
for i in range(2, int(math.sqrt(N)) + 1):
    if is_prime[i]:
        for j in range(i * i, N, i):
            is_prime[j] = False

class Solution:
    def minOperations(self, n: int, m: int) -> int:
        if is_prime[n] or is_prime[m]:
            return -1
        str_n = str(n)
        str_m = str(m)
        ln = len(str_n)

        dist = defaultdict(lambda: float('inf'))
        dist[str_n] = n
        hp = []
        heappush(hp, (n, str_n))  # (cost, state)
        while hp:
            d, cur = heappop(hp)
            if dist[cur] < d:
                continue
            if cur == str_m:
                return d
            lst = list(map(int, cur))
            nxt = []
            for j in range(len(str(int(cur)))):
                i = ln - 1 - j
                if lst[i] < 9: # +1
                    n_lst = lst[:]
                    n_lst[i] += 1
                    nxt.append("".join(map(str, n_lst)))
                if lst[i] > 0: # -1
                    n_lst = lst[:]
                    n_lst[i] -= 1
                    nxt.append("".join(map(str, n_lst)))
            for n_str in nxt:
                val = int(n_str)
                if is_prime[val]:
                    continue
                nd = d + val
                if nd < dist[n_str]:
                    dist[n_str] = nd
                    heappush(hp, (nd, n_str))
        return -1


sol = Solution()
print(sol.minOperations(n = 10, m = 12)) # 85
print(sol.minOperations(n = 4, m = 8)) # -1
print(sol.minOperations(n = 6, m = 2)) # -1
print(sol.minOperations(n = 5637, m = 2034)) # 34943