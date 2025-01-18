from collections import defaultdict

class Rect:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

class Edge:
    def __init__(self, st, ed, rect_id, delta):
        self.st = st
        self.ed = ed
        self.rect_id = rect_id
        self.delta = delta

    def __lt__(self, other):
        return self.st < other.st

class UnionFind:
    def __init__(self, n, areas):
        self.pa = list(range(n))
        self.areas = areas.copy()
    
    def find(self, x):
        while self.pa[x] != x:
            x = self.pa[x]
        return x
    
    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return
        if self.areas[fx] < self.areas[fy]:
            fx, fy = fy, fx
        self.pa[fy] = fx
        self.areas[fx] += self.areas[fy]

while True:
    try:
        n = int(input())
    except EOFError:
        break

    rects = []
    areas = []
    for _ in range(n):
        x, y, w, h = map(int, input().split())
        rects.append(Rect(x, y, x+w, y+h))
        areas.append(w*h)

    uf = UnionFind(n, areas)

    xSet, ySet = set(), set()
    for rect in rects:
        xSet.add(rect.x1)
        xSet.add(rect.x2)
        ySet.add(rect.y1)
        ySet.add(rect.y2)

    xSorted, ySorted = list(sorted(xSet)), list(sorted(ySet))
    xMap = {x : i for i, x in enumerate(xSorted, 1)}
    yMap = {y : i for i, y in enumerate(ySorted, 1)}

    xLines = defaultdict(list)
    yLines = defaultdict(list)
    for rect_id, rect in enumerate(rects):
        xLines[xMap[rect.x1]].append(Edge(yMap[rect.y1], yMap[rect.y2], rect_id, 1))
        xLines[xMap[rect.x2]].append(Edge(yMap[rect.y1], yMap[rect.y2], rect_id, -1))
        yLines[yMap[rect.y1]].append(Edge(xMap[rect.x1], xMap[rect.x2], rect_id, 1))
        yLines[yMap[rect.y2]].append(Edge(xMap[rect.x1], xMap[rect.x2], rect_id, -1))


    for x, edges in xLines.items():
        edges.sort()
        e1 = edges[0]
        for e2 in edges[1:]:
            if e1.st <= e2.st <= e1.ed:
                uf.union(e1.rect_id, e2.rect_id)
                e1.ed = max(e1.ed, e2.ed)
            else:
                e1 = e2

    for y, edges in yLines.items():
        edges.sort()
        e1 = edges[0]
        for e2 in edges[1:]:
            if e1.st <= e2.st <= e1.ed:
                uf.union(e1.rect_id, e2.rect_id)
                e1.ed = max(e1.ed, e2.ed)
            else:
                e1 = e2

    print(max(uf.areas))