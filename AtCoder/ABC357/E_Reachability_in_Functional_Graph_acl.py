"""
    有向基環樹(pseudotree)
"""
from atcoder.scc import *

N = int(input())
A = list(map(int, input().split()))

G = SCCGraph(N)
for i in range(N):
    G.add_edge(i, A[i] - 1)

res = [0] * N
for g in G.scc()[::-1]:
    if len(g) > 1: # 環
        for x in g:
            res[x] = len(g)
    else:
        x = g[0]
        fa = A[x] - 1，
        res[x] = res[fa] + 1
print(sum(res))