n = int(input())
c = [int(input()) for _ in range(n)]
tot = sum(c)

g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    u, v = u - 1, v - 1
    g[u].append((v, w))
    g[v].append((u, w))

sz = [0] * n
dep = [0] * n
f = [0] * n
st = [(0, -1, True)]
while st:
    u, fa, flag = st.pop()
    if flag:
        sz[u] = c[u]
        st.append((u, fa, False))
        for v, w in g[u]:
            if v == fa:
                continue
            dep[v] = dep[u] + 1
            st.append((v, u, True))
    else:
        for v, w in g[u]:
            if v == fa:
                continue
            sz[u] += sz[v]
            f[u] += f[v] + w * sz[v]

ans = float('inf')
st = [(0, -1)]
while st:
    u, fa = st.pop()
    ans = min(ans, f[u])
    for v, w in g[u]:
        if v == fa:
            continue
        f[v] = f[u] - sz[v] * w + (tot - sz[v]) * w
        st.append((v, u))

print(ans)