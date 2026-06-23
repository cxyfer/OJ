class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.fa = list(range(n))
        self.sz = [1] * n
        # dis[x] = potential(x) ^ potential(fa[x])
        self.dis = [0] * n

    def find(self, x: int) -> int:
        """回傳 x 的根，同時做路徑壓縮並更新 dis[x] 為 x 到根的位勢差。"""
        fa = self.fa
        path = []
        curr = x
        while fa[curr] != curr:
            path.append(curr)
            curr = fa[curr]

        root = curr
        for node in reversed(path):
            self.dis[node] ^= self.dis[fa[node]]
            fa[node] = root
        return root

    def potential(self, x: int) -> int:
        """回傳 potential(x) - potential(fa[x])"""
        self.find(x)
        return self.dis[x]

    def union(self, x: int, y: int, w: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        dx, dy = self.dis[x], self.dis[y]
        if rx == ry:
            # x 和 y 在同一集合，不做合併
            return (dy ^ dx) == w

        if self.sz[rx] < self.sz[ry]:  # fa[rx] = ry
            # rx <------- ry
            # |           |
            # | dx        | dy
            # ↓           ↓
            # x --------> y
            # => pot(rx) - pot(ry) = dy - w - dx
            self.fa[rx] = ry
            self.dis[rx] = dy ^ w ^ dx
            self.sz[ry] += self.sz[rx]
        else:  # fa[ry] = rx
            # rx -------> ry
            # |           |
            # | dx        | dy
            # ↓     w     ↓
            # x --------> y
            # => pot(ry) - pot(rx) = w - dy + dx
            self.fa[ry] = rx
            self.dis[ry] = w ^ dy ^ dx
            self.sz[rx] += self.sz[ry]
        return True


def solve() -> None:
    n, q = map(int, input().split())

    edges = []
    deg = [0] * n
    for _ in range(n - 1):
        u, v = map(lambda x: int(x) - 1, input().split())
        edges.append((u, v))
        deg[u] += 1
        deg[v] += 1

    uf = UnionFind(n)
    for _ in range(q):
        u, v, x = map(int, input().split())
        u, v = u - 1, v - 1
        if not uf.union(u, v, x):
            print("No")
            return

    d = uf.dis
    parity = [0] * n
    s = 0
    for u in range(n):
        fu = uf.find(u)
        if deg[u] & 1:
            s ^= d[u]
            parity[fu] ^= 1

    # 避免在 uf.dis 上修改破壞 uf 的結構，複製一份。
    # 注意需要在前面的路徑壓縮完成後複製才能保證正確性。
    d = d.copy()  
    if s != 0:
        for u in range(n):
            if uf.find(u) == u and parity[u] == 1:
                for v in range(n):
                    if uf.find(v) == u:
                        d[v] ^= s
                break

    ans = [d[u] ^ d[v] for u, v in edges]
    print("Yes")
    print(*ans, sep=" ")


if __name__ == "__main__":
    solve()