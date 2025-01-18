"""
    UVA 的輸入格式有問題，需要用類似 cin() 的方式讀取輸入

    Kruskal's algorithm 在 ZeroJudge 會 MLE ，以為是這個問題除錯了很久
"""
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
    # buildings = [list(map(int, input().split())) for _ in range(N)]
    buildings = [[int(cin()) for _ in range(2)] for _ in range(N)]
    # M = int(input())
    M = int(cin())
    # DSU
    pa = [i for i in range(N)]
    def find(x):
        if pa[x] != x:
            pa[x] = find(pa[x])
        return pa[x]
    def union(x, y):
        fx, fy = find(x), find(y)
        if fx != fy:
            pa[fx] = fy
            return True
        return False
    # Kruskal's algorithm
    cnt = 0
    for _ in range(M):
        u, v = int(cin())-1, int(cin())-1
        if union(u, v):
            cnt += 1
    edges = []
    for i in range(N):
        x1, y1 = buildings[i]
        for j in range(i + 1, N):
            x2, y2 = buildings[j]
            cost = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            edges.append((cost, i, j))
    heapify(edges)
    ans = 0
    while edges:
        cost, u, v = heappop(edges)
        if union(u, v):
            ans += cost
            cnt += 1
            if cnt == N - 1:
                break
    print(f"{ans:.2f}")