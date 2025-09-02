N = int(input())
K = list(map(int, input().split()))

s = sum(K)
ans = float("inf")
for i in range(1 << N):
    cur = 0
    for j in range(N):
        if i & (1 << j):
            cur += K[j]
    ans = min(ans, max(cur, s - cur))

print(ans)
