import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

MAX_N = int(5e4 + 5)
is_prime = [True] * MAX_N
is_prime[0] = is_prime[1] = False
for i in range(2, MAX_N):
    if is_prime[i]:
        for j in range(i * i, MAX_N, i):
            is_prime[j] = False

class Solution:
    def primeSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        primes = [(i, x) for i, x in enumerate(nums) if is_prime[x]]
        m = len(primes)
        if m < 2:
            return 0
        ans = left = 0
        q_mn, q_mx = deque(), deque()
        for right, (i, x) in enumerate(primes):
            while q_mn and q_mn[-1][1] >= x:
                q_mn.pop()
            while q_mx and q_mx[-1][1] <= x:
                q_mx.pop()
            q_mn.append((right, x))
            q_mx.append((right, x))

            while q_mx[0][1] - q_mn[0][1] > k:
                left += 1
                while left > q_mx[0][0]:
                    q_mx.popleft()
                while left > q_mn[0][0]:
                    q_mn.popleft()

            if left < right:
                L = primes[right - 1][0] - (primes[left - 1][0] + 1 if left - 1 >= 0 else 0) + 1
                R = (primes[right + 1][0] - 1 if right + 1 < m else n - 1) - primes[right][0] + 1
                ans += L * R
        return ans

sol = Solution()
print(sol.primeSubarray([1,2,3], 1)) # 2
print(sol.primeSubarray([2,3,5,7], 3)) # 4