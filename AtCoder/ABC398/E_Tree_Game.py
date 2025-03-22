import sys

def answer(text):
    print(text)
    sys.stdout.flush()

N = int(input())

g = [[] for _ in range(N+1)]
edges = set()
dist = [[float('inf')] * (N + 1) for _ in range(N + 1)]
for i in range(1, N+1):
    dist[i][i] = 0
for _ in range(N-1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
    dist[u][v] = 1
    dist[v][u] = 1
    edges.add((u, v))  # u < v

# Floyd-Warshall
for k in range(1, N + 1):
    for i in range(1, N + 1):
        if dist[i][k] == float('inf'):
            continue
        for j in range(1, N+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

moves = set()
for u in range(1, N + 1):
    for v in range(u + 1, N + 1):
        if (u, v) in edges:
            continue
        if dist[u][v] & 1:
            moves.add((u, v))

if len(moves) & 1:
    answer("First")
    flag = True
else:
    answer("Second")
    flag = False

while True:
    if flag:
        i, j = moves.pop()
        answer(f"{i} {j}")
    else:
        i, j = map(int, input().split())
        if i == -1 and j == -1:
            break
        moves.remove((i, j))
    flag = not flag