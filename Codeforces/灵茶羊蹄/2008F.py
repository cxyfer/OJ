"""
枚舉右維護左 + 乘法反元素
"""

MOD = int(1e9 + 7)
t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))

    ans = 0
    s = 0
    for a in A:
        ans = (ans + s * a) % MOD
        s = (s + a) % MOD

    ans = (ans * pow(n * (n - 1) // 2, MOD - 2, MOD)) % MOD
    print(ans)