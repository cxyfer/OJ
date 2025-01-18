n = int(input())
W = list(map(int, input().split()))
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)

ans = float('-inf')
def dfs(u, fa):
    global ans
    res = W[u]
    for v in g[u]:
        if v == fa:
            continue
        res += max(0, dfs(v, u))
    ans = max(ans, res)
    return res

dfs(0, -1)
print(ans)