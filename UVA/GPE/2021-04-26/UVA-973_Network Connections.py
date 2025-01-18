class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.size[x] > self.size[y]:
                x, y = y, x
            self.parent[x] = y
            self.size[y] += self.size[x]

t = int(input())

input()

for _ in range(t):
    n = int(input())
    uf = UnionFind(n + 1)
    ans = [0, 0]
    while True:
        try:
            line = input().strip()
            if line == '':
                break
            op, u, v = line.split()
        except:
            break
        u, v = int(u), int(v)
        if op == 'c':
            uf.union(u, v)
        else:
            ans[uf.find(u) == uf.find(v)] += 1

    print(f'{ans[1]},{ans[0]}')
    if _ != t - 1:
        print()