from math import comb
MOD = 100
n = int(input())
print(comb(2 * n, n) // (n + 1) % MOD)