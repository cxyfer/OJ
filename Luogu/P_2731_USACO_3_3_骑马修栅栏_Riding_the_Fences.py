from collections import defaultdict

m = int(input())
g = defaultdict(list)
deg = defaultdict(int)
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
    deg[u] += 1
    deg[v] += 1

odds = [u for u, val in deg.items() if val & 1]
if odds:
    st = min(odds)
else:
    st = min(g.keys())

for u in g:
    g[u].sort()

ans = []
def dfs(u):
    while g[u]:
        v = g[u].pop(0)
        g[v].remove(u)
        dfs(v)
    ans.append(u)
dfs(st)
print(*ans[::-1], sep='\n')