def solve():
    n, m = map(int, input().split())

    edges = [tuple(map(int, input().split())) for _ in range(m)]
    edges.sort(key=lambda x: x[2])

    pa = list(range(n + 1))
    sz = [1] * (n + 1)
    cnt = n

    def find(x: int) -> int:
        while pa[x] != x:
            pa[x] = pa[pa[x]]
            x = pa[x]
        return x

    def union(x: int, y: int) -> bool:
        nonlocal cnt
        fx, fy = find(x), find(y)
        if fx == fy:
            return False
        if sz[fx] < sz[fy]:
            fx, fy = fy, fx
        pa[fy] = fx
        sz[fx] += sz[fy]
        cnt -= 1
        return True

    cost = 0
    for u, v, w in edges:
        u, v = u - 1, v - 1
        if union(u, v):
            cost += w
            if cnt == 1:
                break
    print(cost if cnt == 1 else -1)


if __name__ == "__main__":
    solve()
