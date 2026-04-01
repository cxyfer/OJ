MAX_N = int(1e5 + 5)
MOD = int(1e9 + 7)

fact = [1] * (MAX_N + 1)
for i in range(2, MAX_N + 1):
    fact[i] = fact[i - 1] * i % MOD
invf = [1] * (MAX_N + 1)
invf[-1] = pow(fact[-1], -1, MOD)
for i in range(MAX_N, 0, -1):
    invf[i - 1] = invf[i] * i % MOD

def comb(n, k):
    if k < 0 or k > n:
        return 0
    return fact[n] * invf[k] % MOD * invf[n - k] % MOD

def perm(n, k):
    if k < 0 or k > n:
        return 0
    return fact[n] * invf[n - k] % MOD