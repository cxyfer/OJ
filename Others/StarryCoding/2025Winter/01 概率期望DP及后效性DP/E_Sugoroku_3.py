"""
    期望DP
    
    f[i] 表示從 i 到 n-1 的期望步數 (0-indexed)
    f[i] = 1 + sum_j=i^{i+A[i]}(f[j]) / (A[i] + 1)
    => (A[i] + 1) * f[i] = (A[i] + 1) + sum_j=i^{i+A[i]}(f[j])
    => A[i] * f[i] = (A[i] + 1) + sum_j={i+1}^{i+A[i]}(f[j])
    => f[i] = (A[i] + 1 + sum_j={i+1}^{i+A[i]}(f[j])) / A[i]
"""
MOD = 998244353

n = int(input())
A = list(map(int, input().split()))

f = [0] * n
suf = [0] * (n + 1)

for i in range(n - 2, -1, -1):
    f[i] = (suf[i + 1] - suf[i + A[i] + 1] + A[i] + 1) * pow(A[i], MOD - 2, MOD)
    f[i] %= MOD
    suf[i] = (suf[i + 1] + f[i]) % MOD

print(f[0])