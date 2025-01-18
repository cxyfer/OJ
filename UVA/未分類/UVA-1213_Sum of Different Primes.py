# import sys
# from functools import cache
# sys.setrecursionlimit(1 << 20)

MAXN = 1120 + 5
is_prime = [True] * MAXN
is_prime[0] = is_prime[1] = False
primes = []
for i in range(2, MAXN):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, MAXN, i):
            is_prime[j] = False

# @cache
# def solve(i: int, n: int, k: int) -> int:
#     if k == 0:
#         return 1 if n == 0 else 0
#     if n < 2 or i >= len(primes) or primes[i] > n:
#         return 0
#     res = solve(i + 1, n, k) # 不選擇當前質數
#     if n >= primes[i]: # 選擇當前質數
#         res += solve(i + 1, n - primes[i], k - 1)
#     return res

dp = [[0] * (14 + 1) for _ in range(MAXN)]
dp[0][0] = 1
for p in primes:
    for i in range(MAXN - 1, p - 1, -1):
        for j in range(14, 0, -1):
            dp[i][j] += dp[i - p][j - 1]

while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break
    print(dp[n][k])