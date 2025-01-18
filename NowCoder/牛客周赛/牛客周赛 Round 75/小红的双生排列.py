MOD = int(1e9 + 7)

n = int(input())

o = (n + 1) // 2
e = n // 2

fact = [1] * (o + 1)
for i in range(1, o + 1):
    fact[i] = fact[i - 1] * i % MOD

if n & 1:
    print(fact[o] * fact[e] % MOD)
else:
    print(fact[o] * fact[e] * 2 % MOD)