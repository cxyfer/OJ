MAXN = int(1e7) + 5
is_prime = [True] * MAXN
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAXN ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAXN, i):
            is_prime[j] = False
primes = [i for i in range(MAXN) if is_prime[i]]

while True:
    n = int(input())
    if n == 0: break
    ans = -1
    cnt = 0
    for p in primes:
        if p * p > n: break
        if n % p == 0:
            cnt += 1
            ans = p
            while n % p == 0:
                n //= p
    if n > 1:
        ans = n
        cnt += 1
    print(ans if cnt > 1 else -1)