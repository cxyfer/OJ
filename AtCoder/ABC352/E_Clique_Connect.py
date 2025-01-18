"""
    Minimum Spanning Tree (MST) problem
    Kruskal's algorithm + Disjoint Set Union (DSU)
"""
from atcoder.dsu import DSU

N, M = map(int, input().split())
edges = []
for _ in range(M):
    k, c = map(int, input().split()) # k vertices, cost c
    A = list(map(int, input().split())) # subset 
    edges.append((c, A))
edges.sort(key=lambda x: x[0]) # 從 cost 最小的邊開始添加

ans = 0
uf = DSU(N)

for c, A in edges:
    u = A[0]
    for i in range(1, len(A)):
        v = A[i]
        if not uf.same(u-1, v-1):
            uf.merge(u-1, v-1)
            ans += c
print(ans if len(uf.groups()) == 1 else -1) # is connected
