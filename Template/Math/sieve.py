import math

MAX_N = int(5e5 + 5)

# primes
is_prime = [True] * (MAX_N + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, math.isqrt(MAX_N) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX_N + 1, i):
            is_prime[j] = False
primes = [x for x in range(2, MAX_N) if is_prime[x]]

# least prime factor
spf = [0] * (MAX_N + 1)
for i in range(2, MAX_N + 1):
    if spf[i] == 0:
        spf[i] = i
        for j in range(i * i, MAX_N + 1, i):
            if spf[j] == 0:
                spf[j] = i


def prime_factorization(x: int) -> list[int]:
    factors = []
    while x > 1:
        p = spf[x]
        factors.append(p)
        while spf[x] == p:
            x //= p
    return factors


print(prime_factorization(100))  # [2, 5]
