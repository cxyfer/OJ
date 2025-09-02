"""
    快速幂 + 乘法反元素
    N = 5
    x = 1
    NNNNN = 55555 = N * (11111)
    = N * (10^0 + 10^x + 10^2x + 10^3x + 10^4x)
    = N * (10^(Nx) - 1) / (10^x - 1)
"""
N = int(input())
x = len(str(N))
MOD = 998244353

p1 = pow(10, N * x, MOD) - 1
p2 = pow(10, x, MOD) - 1
inv = pow(p2, MOD - 2, MOD)

print(N * p1 * inv % MOD)