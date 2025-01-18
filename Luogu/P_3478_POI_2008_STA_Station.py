import sys
input = lambda: sys.stdin.readline().strip()
print = lambda val: sys.stdout.write(str(val) + "\n")

n = int(input())

g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    g[u].append(v)
    g[v].append(u)

sz = [1] * n
dep = [0] * n
f = [0] * n
st = [(0, -1, True)]
while st:
    u, fa, flag = st.pop()
    if flag:
        st.append((u, fa, False))
        f[u] = dep[u]
        for v in g[u]:
            if v == fa:
                continue
            st.append((v, u, True))
            dep[v] = dep[u] + 1
    else:
        for v in g[u]:
            if v == fa:
                continue
            sz[u] += sz[v]
            f[u] += f[v]

st = [(0, -1)]
while st:
    u, fa = st.pop()
    for v in g[u]:
        if v == fa:
            continue
        f[v] = f[u] - sz[v] + (n - sz[v])
        st.append((v, u))

ans = 0
for i in range(n):
    if f[i] > f[ans]:
        ans = i
print(ans + 1)