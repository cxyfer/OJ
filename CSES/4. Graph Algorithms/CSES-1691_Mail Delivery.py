import sys
input = lambda: sys.stdin.readline().strip()
print = lambda val: sys.stdout.write(str(val) + "\n")

n, m = map(int, input().split())
g = [[] for _ in range(n)]
deg = [0] * n

for eid in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    g[u].append((v, eid))
    g[v].append((u, eid))
    deg[u] += 1
    deg[v] += 1


if any(deg[u] & 1 for u in range(n)):
    print("IMPOSSIBLE")
    exit()


for u in range(n):
    g[u].sort(key=lambda x: x[1])

path = []
used = [False] * m

st = [0]
while st:
    u = st[-1]
    while g[u]:
        v, eid = g[u].pop()
        if used[eid]:
            continue
        used[eid] = True
        st.append(v)
        break
    else:
        path.append(u + 1)
        st.pop()

if len(path) != m + 1:
    print("IMPOSSIBLE")
else:
    path.reverse()
    print(" ".join(map(str, path)))