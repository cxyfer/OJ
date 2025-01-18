"""
    DP + 埃氏篩(Sieve of Eratosthenes)
    這裡偷懶寫了 Top-Down 的 DP，用 cache 做 memoization
    Bottom-Up 的 DP 可以參考 C++ 版本
    不過這題主要難點在輸出格式，調了很久才對。
"""
from collections import Counter
from functools import cache

N = 101
is_prime = [True] * N
is_prime[0] = is_prime[1] = False
for i in range(2, N):
    if is_prime[i]:
        for j in range(i*i, N, i):
            is_prime[j] = False
primes = [i for i in range(N) if is_prime[i]]

@cache
def f(n: int) -> Counter:
    cnt = Counter()
    if n == 1:
        return cnt
    tmp = n
    for p in primes:
        if tmp == 1:
            break
        while tmp % p == 0:
            cnt[p] += 1
            tmp //= p
    return cnt + f(n - 1)

while True:
    n = int(input())
    if n == 0:
        break
    cnt = f(n)
    mx = max(cnt)
    print(f"{n:>3}! =", end='')
    for i, p in enumerate(primes):
        if p > mx:
            break
        if i > 0 and i % 15 == 0:
            print("\n      ", end='')
        print(f"{cnt[p]:>3}", end='')
    print()