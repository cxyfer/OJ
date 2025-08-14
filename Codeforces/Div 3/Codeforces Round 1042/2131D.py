t = int(input())

def solve():
    n = int(input())
    g = [[] for _ in range(n)]
    deg = [0] * n
    for _ in range(n - 1):
        u, v = map(lambda x: int(x) - 1, input().split())
        g[u].append(v)
        g[v].append(u)
        deg[u] += 1
        deg[v] += 1

    if n <= 2:
        print(0)
        return
    
    leafs = sum(deg[i] == 1 for i in range(n))
    ans = leafs
    for u in range(n):
        cur = 0  # 與 u 相鄰的 leaf 數
        for v in g[u]:
            if deg[v] == 1:
                cur += 1
        ans = min(ans, leafs - cur)
    print(ans)

for _ in range(t):
    solve()