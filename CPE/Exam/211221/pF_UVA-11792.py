t = int(input())

for _ in range(t):
    n, s = map(int, input().split())
    g = [set() for _ in range(n + 1)]
    cnt = [0] * (n + 1)

    for _ in range(s):
        arr = list(map(int, input().split()))
        arr = arr[:-1] # remove the last element
        cnt[arr[0]] += 1
        for i in range(1, len(arr)):
            u, v = arr[i - 1], arr[i]
            g[u].add(v)
            g[v].add(u)
            cnt[v] += 1

    importants = [x for x in range(1, n + 1) if cnt[x] > 1]
    ans = importants[0]
    mn = float("inf") # minimum distance
    for x in importants: # BFS from each important node
        q = [(x, 0)]
        visited = [False] * (n + 1)
        dist = [float("inf")] * (n + 1)
        dist[x] = 0
        visited[x] = True
        while q and not all(visited[y] for y in importants):
            u, d = q.pop(0)
            for v in g[u]:
                if not visited[v]:
                    visited[v] = True
                    dist[v] = d + 1
                    q.append((v, d + 1))
        d_sum = sum(dist[y] for y in importants)
        if d_sum < mn:
            mn = d_sum
            ans = x
    print(f"Krochanska is in: {ans}")
