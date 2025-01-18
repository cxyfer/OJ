from collections import deque

kase = 1
while True:
    n = int(input())
    if n == 0:
        break
    s = int(input())
    g = [[] for _ in range(n + 1)]
    while True:
        u, v = map(int, input().split())
        if u == 0 and v == 0:
            break
        g[u].append(v)

    q = deque([(s, 0)])
    dist = [0] * (n + 1)
    while q:
        u, d = q.popleft()
        if d < dist[u]: # Lazy Deletion
            continue
        for v in g[u]:
            if dist[v] < d + 1:
                dist[v] = d + 1
                q.append((v, d + 1))
    
    mx = max(dist)
    idx = dist.index(mx)
    print(f"Case {kase}: The longest path from {s} has length {mx}, finishing at {idx}.")
    print()
    kase += 1