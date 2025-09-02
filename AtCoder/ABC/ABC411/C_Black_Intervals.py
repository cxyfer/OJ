N, Q = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
vis = [0] * (N + 2)
for x in A:
    if vis[x - 1] and vis[x + 1]:
        ans += 1 if vis[x] else -1
    elif not vis[x - 1] and not vis[x + 1]:
        ans += -1 if vis[x] else 1
    vis[x] ^= 1
    print(ans)