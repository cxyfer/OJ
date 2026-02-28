from heapq import heappop, heappush


def solve():
    n, m, t = map(int, input().split())
    t -= 1

    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u, v = u - 1, v - 1
        g[u].append((v, w))
        g[v].append((u, w))

    def dijkstra(s):
        dist = [float("inf")] * n
        dist[s] = 0
        hp = [(0, s)]
        while hp:
            d, u = heappop(hp)
            if d > dist[u]:
                continue
            for v, w in g[u]:
                nd = dist[u] + w
                if nd < dist[v]:
                    dist[v] = nd
                    heappush(hp, (nd, v))
        return dist

    dist_s = dijkstra(0)
    dist_t = dijkstra(t)
    ans = dist_s[t] + dist_t[0]
    print(ans if ans != float("inf") else -1)


if __name__ == "__main__":
    solve()
