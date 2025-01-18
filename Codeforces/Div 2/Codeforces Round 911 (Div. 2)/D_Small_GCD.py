"""
    考慮貢獻
"""

# 預先計算每個數字的因數
MAX_N = 100000
factor = [[] for _ in range(MAX_N+1)]
for i in range(1, MAX_N+1):
    for j in range(i, MAX_N+1, i):
        factor[j].append(i)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = [float("-inf")] + list(map(int, input().split()))
    A.sort()

    c = [0] * (MAX_N+1)
    f = [0] * (MAX_N+1)
    for i in range(1, N+1):
        for x in factor[A[i]]:
            f[x] += c[x] * (N - i)
            c[x] += 1
    ans = 0
    for i in range(MAX_N, 0, -1):
        for j in range(i+i, MAX_N+1, i):
            f[i] -= f[j]
        ans += f[i] * i
    print(ans)
