from collections import deque

def solve():
    n = int(input())
    colors = list(map(int, input().split()))
    g = [[] for _ in range(n)]
    deg = [0] * n
    for _ in range(n - 1):
        u, v = map(lambda x: int(x) - 1, input().split())
        g[u].append(v)
        g[v].append(u)
        deg[u] += 1
        deg[v] += 1

    if n == 1:
        print(0)
        return

    ans = colors.count(0)
    q = deque([u for u in range(n) if deg[u] == 1 and colors[u] == 0])
    while q:
        u = q.popleft()
        ans -= 1
        for v in g[u]:
            deg[v] -= 1
            if deg[v] == 1 and colors[v] == 0:
                q.append(v)
    print(ans)

if __name__ == "__main__":
    solve()