import sys
input = sys.stdin.readline

MOD = 998244353
MAX_N = int(2e5 + 5)
fact = [1] * (MAX_N + 1)
for i in range(1, MAX_N + 1):
    fact[i] = (fact[i - 1] * i) % MOD
invf = [0] * (MAX_N + 1)
invf[MAX_N] = pow(fact[MAX_N], MOD - 2, MOD)
for i in range(MAX_N - 1, -1, -1):
    invf[i] = (invf[i + 1] * (i + 1)) % MOD

def comb(a, b):
    return fact[a] * invf[b] * invf[a - b] % MOD

# Catalan Number: Catalan(n) = C(2n, n) / (n + 1)
def Catalan(n):  
    return comb(2 * n, n) * pow(n + 1, MOD - 2, MOD) % MOD

if __name__ == '__main__':
    T = int(input())
    for kase in range(1, T + 1):
        n = int(input())
        ans = (Catalan(n) - Catalan(n - 1)) % MOD
        print(f"Case #{kase}: {ans}")