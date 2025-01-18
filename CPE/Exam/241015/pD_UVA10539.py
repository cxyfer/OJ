from math import isqrt
from bisect import bisect_left, bisect_right

MAXN = int(1e12)
MAXN_SQRT = isqrt(MAXN)
is_prime = [True] * (MAXN_SQRT + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, MAXN_SQRT + 1):
    if is_prime[i]:
        for j in range(i * i, MAXN_SQRT + 1, i):
            is_prime[j] = False

almost_primes = []
for i in range(2, MAXN_SQRT + 1):
    if is_prime[i]:
        x = i * i
        while x <= MAXN:
            almost_primes.append(x)
            x *= i
almost_primes.sort()

t = int(input())
for _ in range(t):
    lo, hi = map(int, input().split())
    print(bisect_right(almost_primes, hi) - bisect_left(almost_primes, lo))