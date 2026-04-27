"""
P1955 [NOI2015] 程序自动分析
https://www.luogu.com.cn/problem/P1955
1. 離線作法：併查集 + 離散化
2. 在線(偽)作法：併查集 + 啟發式合併
   因為還是需要離散化，因此還是需要讀取所有變數，但可以中途給出答案
"""


class UnionFind:
    __slots__ = ["n", "pa", "sz", "cnt"]

    def __init__(self, n: int):
        self.n = n
        self.pa = list(range(n))  # 父節點
        self.sz = [1] * n  # 連通分量大小
        self.cnt = n  # 連通分量數量

    def find(self, x: int) -> int:
        while self.pa[x] != x:
            self.pa[x] = self.pa[self.pa[x]]
            x = self.pa[x]
        return x

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


def solve1():
    n = int(input())
    Xs = set()
    constraints = [[] for _ in range(2)]
    for _ in range(n):
        a, b, e = map(int, input().split())
        constraints[e].append((a, b))
        Xs.add(a)
        Xs.add(b)

    Xs = sorted(Xs)
    mp = {x: i for i, x in enumerate(Xs)}
    m = len(Xs)

    uf = UnionFind(m)
    for a, b in constraints[1]:
        uf.union(mp[a], mp[b])
    for a, b in constraints[0]:
        if uf.find(mp[a]) == uf.find(mp[b]):
            print("NO")
            break
    else:
        print("YES")


def solve2():
    n = int(input())
    Xs = set()
    constraints = []
    for _ in range(n):
        a, b, e = map(int, input().split())
        constraints.append((a, b, e))
        Xs.add(a)
        Xs.add(b)

    Xs = sorted(Xs)
    mp = {x: i for i, x in enumerate(Xs)}
    m = len(Xs)

    fa = list(range(m))  # 父節點
    diffs = [set() for _ in range(m)]  # diffs[u] 表示與需與 u 不同的節點集合

    def find(x):
        path = []
        curr = x
        while fa[curr] != curr:
            path.append(curr)
            curr = fa[curr]
        root = curr
        for node in reversed(path):
            fa[node] = root
        return root

    for a, b, e in constraints:
        x, y = mp[a], mp[b]
        fx, fy = find(x), find(y)
        if e == 1:  # 相等關係
            if fx == fy:
                continue
            # 啟發式合併，讓 fy 是較小的集合
            if len(diffs[fx]) < len(diffs[fy]):
                fx, fy = fy, fx
            if any(find(u) == fx for u in diffs[fy]):
                print("NO")
                break
            fa[fy] = fx
            diffs[fx].update(diffs[fy])
        else:  # 相異關係
            if fx == fy:
                print("NO")
                break
            diffs[fx].add(y)
            diffs[fy].add(x)
    else:
        print("YES")


# solve = solve1
solve = solve2


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
