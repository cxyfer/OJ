import math

MAX_N = int(5e5 + 5)

def sieve(MAX_N: int) -> list[int]:
    is_prime = [True] * (MAX_N + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, math.isqrt(MAX_N) + 1):
        if is_prime[i]:
            for j in range(i * i, MAX_N + 1, i):
                is_prime[j] = False
    primes = [x for x in range(2, MAX_N) if is_prime[x]]
    return primes