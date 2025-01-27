from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    R = list(map(lambda x: int(x) - 1, input().split()))

    ind = [0] * n
    for i, r in enumerate(R):
        ind[r] += 1

    dist = [0] * n  # 到基環樹上環的距離
    q = deque()
    for u in range(n):
        if ind[u] == 0:
            dist[u] = 1
            q.append(u)

    while q:
        u = q.popleft()
        ind[R[u]] -= 1
        if ind[R[u]] == 0:
            dist[R[u]] = dist[u] + 1
            q.append(R[u])
    
    print(max(dist) + 2)