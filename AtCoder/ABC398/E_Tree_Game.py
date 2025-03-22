import sys
from collections import deque

def answer(text):
    print(text)
    sys.stdout.flush()

N = int(input())
g = [[] for _ in range(N + 1)]
edges = set()
for _ in range(N-1):
    u, v = map(int, input().split())
    edges.add((min(u, v), max(u, v)))
    g[u].append(v)
    g[v].append(u)

# Bipartite
color = [-1] * (N + 1)
q = deque([1])
color[1] = 0
while q:
    u = q.popleft()
    for v in g[u]:
        if color[v] != -1:
            continue
        color[v] = 1 ^ color[u]
        q.append(v)

A = [u for u in range(1, N + 1) if color[u] == 0]
B = [u for u in range(1, N + 1) if color[u] == 1]

moves = set()
for a in A:
    for b in B:
        u, v = min(a, b), max(a, b)
        if (u, v) in edges:
            continue
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