import sys
input = lambda: sys.stdin.readline().strip()
print = lambda val: sys.stdout.write(str(val) + "\n")

from collections import defaultdict

def floyd_warshall(g):
    nodes = list(g.keys())
    for k in nodes:
        for i in nodes:
            if g[i][k] == float("inf"):
                continue
            for j in nodes:
                if g[k][j] == float("inf"):
                    continue
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])
    return g

answer = []
while True:
    n = int(input())
    if n == 0:
        break

    g1 = defaultdict(lambda: defaultdict(lambda: float("inf")))
    g2 = defaultdict(lambda: defaultdict(lambda: float("inf")))

    for _ in range(n):
        u, *nodes = map(int, input().split())
        g1[u][u] = 0
        for v in nodes:
            g1[u][v] = 1
            g1[v][u] = 1
            g1[v][v] = 0

    for _ in range(n):
        u, *nodes = map(int, input().split())
        g2[u][u] = 0
        for v in nodes:
            g2[u][v] = 1
            g2[v][v] = 0

    A, B = map(int, input().split())

    g1 = floyd_warshall(g1)
    g2 = floyd_warshall(g2)

    flag = True
    for u in g1.keys():
        for v in g2.keys():
            if g2[u][v] > g1[u][v] * A + B:
                flag = False
                break
        if not flag:
            break
    
    # print("Yes" if flag else "No")
    answer.append("Yes" if flag else "No")

print("\n".join(answer))
