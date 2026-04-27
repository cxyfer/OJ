class UnionFind:
    __slots__ = ['n', 'pa', 'sz', 'cnt']

    def __init__(self, n: int):
        self.n = n
        self.pa = list(range(n))  # 父節點
        self.sz = [1] * n  # 連通分量大小
        self.cnt = n  # 連通分量數量

    def find(self, x: int) -> int:
        """Recursive version, full path compression"""
        # if self.pa[x] != x:
        #     self.pa[x] = self.find(self.pa[x])
        # return self.pa[x]
        """Iterative version, path halving"""
        while self.pa[x] != x:
            self.pa[x] = self.pa[self.pa[x]]
            x = self.pa[x]
        return x
        """Iterative version, full path compression"""
        # path = []
        # curr = x
        # while self.pa[curr] != curr:
        #     path.append(curr)
        #     curr = self.pa[curr]
        # root = curr
        # for node in reversed(path):
        #     self.pa[node] = root
        # return root

    def union(self, x: int, y: int) -> bool:
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False
        if self.sz[fx] < self.sz[fy]:
            fx, fy = fy, fx
        self.pa[fy] = fx
        self.sz[fx] += self.sz[fy]
        self.cnt -= 1
        return True