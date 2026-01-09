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

    k = max(ans, max(len(layers[d]) for d in layers))

    color = [0] * n
    color[0] = 0
    for d in range(1, max(layers.keys()) + 1):
        arr = layers[d]
        for i, u in enumerate(arr):
            color[u] = i

        nodes = [i for i, u in enumerate(arr) if fa[u] != -1 and color[fa[u]] == color[u]]
        if len(nodes) == 1:
            idx = nodes[0]
            u = arr[idx]
            c = color[u]
            if (m := len(arr)) < k:
                color[u] = m
            else:
                for j, v in enumerate(arr):
                    if color[fa[v]] != c:
                        color[arr[idx]], color[arr[j]] = color[arr[j]], color[arr[idx]]
                        break
        elif len(nodes) >= 2:
            c = color[arr[nodes[0]]]
            for j in range(len(nodes) - 1):
                color[arr[nodes[j]]] = color[arr[nodes[j + 1]]]
            color[arr[nodes[-1]]] = c

    ops = [[] for _ in range(k)]
    for u in range(n):
        ops[color[u]].append(u + 1)

    print(len(ops))
    for op in ops:
        print(len(op), *op)

    tot = sum(len(op) for op in ops)
    assert tot == n, f"tot = {tot}, n = {n}"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
