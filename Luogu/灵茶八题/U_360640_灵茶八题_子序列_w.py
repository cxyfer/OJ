"""
    包含 A[i] 的子序列數量 = 2^(n-1)
"""
n = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7

p = pow(2, n - 1, MOD)

ans = 0
for i in range(n):
    ans += A[i] * p
    ans %= MOD
print(ans)