from collections import deque

N = int(input())
S = input()
T = input()

f = [-1] * 26
for s, t in zip(S, T):
    u, v = ord(s) - ord('a'), ord(t) - ord('a')
    if f[u] != -1:
        if f[u] != v:
            exit(print(-1))
    else:
        f[u] = v
for u in range(26):
    if f[u] == -1:
        f[u] = u

ans = 0
indeg = [0] * 26
for u in range(26):
    v = f[u]
    if u == v: continue
    indeg[v] += 1
    ans += 1

q = deque([u for u, d in enumerate(indeg) if d == 0])
while q:
    u = q.popleft()
    v = f[u]
    if u == v: continue
    indeg[v] -= 1
    if indeg[v] == 0:
        q.append(v)

for u in range(26):
    if indeg[u] == 0: continue
    v = f[u]
    indeg[u] = indeg[v] = 0
    while v != u:
        v = f[v]
        indeg[v] = 0
    ans += 1
print(ans)