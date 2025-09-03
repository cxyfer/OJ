"""
UVA-13204 Count these Permutations
https://vjudge.net/problem/UVA-13204
打表/數學

令 f(N) 表示在 1 ~ N 中，所有滿足條件的排列數。
打表可以得：
f(1) = 1
f(2) = 1
f(3) = 3
f(4) = 4
f(5) = 20
f(6) = 36
f(7) = 252
f(8) = 576
f(9) = 5184
f(10) = 14400
f(11) = 158400

觀察可以得到：
- 當 N 為偶數時，f(N) = f(N - 2) * (N // 2)^2
- 當 N 為奇數時，f(N) = f(N - 1) * N

解遞迴式，可以得到：
f(N) = (N//2)! * (N//2)!     , if N is even
f(N) = (N//2)! * (N//2)! * N , if N is odd
"""
MOD = int(1e9 + 7)
MAX_N = int(1e6 + 5)
fact = [1] * (MAX_N // 2)
for i in range(1, MAX_N // 2):
    fact[i] = fact[i - 1] * i % MOD

while True:
    try:
        N = int(input())
    except EOFError:
        break
    if N & 1:
        print(fact[N // 2] ** 2 * N % MOD)
    else:
        print(fact[N // 2] ** 2 % MOD)

# from itertools import permutations
# import math

# for N in range(1, 11):
#     tgt = math.floor(N * N / 2)
#     ans = 0
#     for perm in permutations(range(1, N + 1)):
#         val = sum(abs(x - i) for i, x in enumerate(perm, 1))
#         if val > tgt:
#             print(perm)
#         elif val == tgt:
#             ans += 1
#     print(f"{N=:2d}: {ans}")