"""
Fermat's Little Theorem:
    a^k mod p = a^(k mod (p-1)) mod p
"""
MOD = int(1e9 + 7)

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    print(pow(a, pow(b, c, MOD - 1), MOD))