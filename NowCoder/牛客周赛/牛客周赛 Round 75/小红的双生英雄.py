N, C, M = map(int, input().split())
heroes = [tuple(map(int, input().split())) for _ in range(N)]
pairs = [tuple(map(int, input().split())) for _ in range(M)]

groups = []
is_pair = [False] * N
for u, v, w in pairs:
    u -= 1
    v -= 1
    is_pair[u] = True
    is_pair[v] = True
    groups.append((u, v, w))
for i in range(N):
    if not is_pair[i]:
        groups.append((i, i, 0))

n = len(groups)
f = [[-float('inf')] * (5) for _ in range(C + 1)]
f[0][0] = 0
for u, v, w in groups:
    cost_u, w_u = heroes[u]
    cost_v, w_v = heroes[v]
    cost_both = cost_u + cost_v
    w_both = w_u + w_v + w

    new_f = [row[:] for row in f]
    for j in range(C + 1):
        for k in range(5):
            if f[j][k] == -float('inf'):
                continue
            new_f[j][k] = max(new_f[j][k], f[j][k])
            if j + cost_u <= C and k + 1 <= 4:
                new_f[j + cost_u][k + 1] = max(new_f[j + cost_u][k + 1], f[j][k] + w_u)
            if u != v and j + cost_v <= C and k + 1 <= 4:
                new_f[j + cost_v][k + 1] = max(new_f[j + cost_v][k + 1], f[j][k] + w_v)
            if u != v and j + cost_both <= C and k + 2 <= 4:
                new_f[j + cost_both][k + 2] = max(new_f[j + cost_both][k + 2], f[j][k] + w_both)
    f = new_f

ans = 0
for j in range(C + 1):
    for k in range(5):
        ans = max(ans, f[j][k])
print(ans)