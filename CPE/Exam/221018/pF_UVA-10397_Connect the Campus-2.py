"""
    輸入格式有問題，需要用類似 cin() 的方式讀取輸入
"""
from math import sqrt
from heapq import *

import sys
buf = sys.stdin.read().split()
cin = lambda: buf.pop(0)
def print(val=""): sys.stdout.write(str(val)+"\n")

while True:
    try:
        # N = int(input())
        N = int(cin())
    except:
        break
    X, Y = [0] * N, [0] * N
    for i in range(N):
        # x, y = map(int, input().split())
        x, y = int(cin()), int(cin())
        X[i], Y[i] = x, y
    # Adjacency matrix
    g = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            g[i][j] = g[j][i] = sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2)
    # M = int(input())
    M = int(cin())
    for _ in range(M):
        # u, v = map(int, input().split())
        u, v = int(cin()), int(cin())
        u -= 1
        v -= 1
        g[u][v] = g[v][u] = 0
    # Prim's algorithm
    cost = [1e9] * N
    cost[0] = 0
    visited = [False] * N
    ans = 0
    hp = [(0, 0)] # (dist, node)
    while hp:
        d, u = heappop(hp)
        if visited[u]:
            continue
        visited[u] = True
        for v in range(N):
            if not visited[v] and cost[v] > g[u][v]:
                cost[v] = g[u][v]
                heappush(hp, (cost[v], v))
    ans = sum(cost)
    print(f"{ans:.2f}")