"""
U360640 灵茶八题 - 子序列 +w+
https://www.luogu.com.cn/problem/U360640

考慮貢獻，包含 A[i] 的子序列數量有 2^(n-1) 個
"""
n = int(input())
A = list(map(int, input().split()))
MOD = int(1e9 + 7)

p = pow(2, n - 1, MOD)

ans = 0
for i in range(n):
    ans += A[i] * p
    ans %= MOD
print(ans)