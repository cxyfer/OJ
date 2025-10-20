"""
均攤 (Amortized)

"""

N, Q = map(int, input().split())

cnt = [0] + [1] * N
last = 1
for _ in range(Q):
    x, y = map(int, input().split())
    ans = 0
    for v in range(last, x + 1):
        ans += cnt[v]
        cnt[y] += cnt[v]
        cnt[v] = 0
    last = max(last, x)
    print(ans)