from itertools import count

def dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

class UnionFind:
    def __init__(self, n):
        self.pa = list(range(n))
        self.sz = [1] * n
        self.cnt = n

    def find(self, x):
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]

    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False
        if self.sz[fx] < self.sz[fy]:
            fx, fy = fy, fx
        self.pa[fy] = fx
        self.sz[fx] += self.sz[fy]
        self.cnt -= 1
        return True

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

    def __lt__(self, other):
        return self.w < other.w

for kase in count(1):
    n = int(input().strip())
    if n == 0:
        break
    points = [tuple(map(int, input().strip().split())) for _ in range(n)]
    input()

    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append(Edge(i, j, dist(points[i], points[j])))
    edges.sort()
    uf = UnionFind(n)
    for edge in edges:
        if uf.union(edge.u, edge.v):
            if uf.find(0) == uf.find(1):
                print(f"Scenario #{kase}")
                print(f"Frog Distance = {edge.w:.3f}")
                print()
                break