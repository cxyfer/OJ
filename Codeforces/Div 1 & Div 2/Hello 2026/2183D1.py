from collections import deque, defaultdict

def solve():
    n = int(input())
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(lambda x: int(x) - 1, input().split())
        g[u].append(v)
        g[v].append(u)

    ans = 0
    q = deque([0])
    dist = [0] * n
    fa = [0] * n
    fa[0] = -1
    while q:
        u = q.popleft()
        for v in g[u]:
            if v == fa[u]:
                continue
            dist[v] = dist[u] + 1
            fa[v] = u
            q.append(v)
        ans = max(ans, sum(1 for v in g[u] if v != fa[u]) + 1)

    layers = defaultdict(list)
    for u in range(n):
        layers[dist[u]].append(u)

    print(max(ans, max(len(layers[d]) for d in layers)))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()