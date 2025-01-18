from math import comb

MOD = int(1e8 + 7)

n = int(input())
print(comb(2 * n, n) // (n + 1) % MOD)