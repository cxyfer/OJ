import sys
sys.setrecursionlimit(int(2e5))

n, m = map(int, input().strip().split())
g = [[] for _ in range(n)]
deg = [0] * n
for idx in range(m):
    u, v = map(lambda x: int(x) - 1, input().strip().split())
    g[u].append((v, idx))
    deg[u] += 1
    deg[v] -= 1

for u in range(n):
    g[u].sort()

st = -1
for u, val in enumerate(deg):
    if val == 1:
        st = u
        break
else:
    st = 0

cnt0 = cnt1 = cnt2 = 0
for u, val in enumerate(deg):
    if val == 0:
        cnt0 += 1
    elif val == 1:
        cnt1 += 1
    elif val == -1:
        cnt2 += 1

is_euler = (cnt0 == n and cnt1 == cnt2 == 0) or (cnt0 == n - 2 and cnt1 == cnt2 == 1)
if not is_euler:
    exit(print("No"))

path = []
used = [False] * m
def dfs(u):
    while g[u]:
        v, idx = g[u].pop(0)
        if used[idx]:
            continue
        used[idx] = True
        dfs(v)
    path.append(u)
dfs(st)

if len(path) == m + 1:
    print(*map(lambda x: x + 1, path[::-1]))
else:
    print("No")