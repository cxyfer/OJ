from functools import cache


def solve():
    N, M = map(int, input().split())
    dist = [[float("inf")] * N for _ in range(N)]
    for u in range(N):
        dist[u][u] = 0

    for _ in range(M):
        u, v, w = map(int, input().split())
        u, v = u - 1, v - 1
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w

    # Floyd-Warshall
    for k in range(N):
        for u in range(N):
            if dist[u][k] == float("inf"):
                continue
            for v in range(N):
                dist[u][v] = min(dist[u][v], dist[u][k] + dist[k][v])

    if any(dist[0][u] == float("inf") for u in range(N)):
        print(-1)
        return

    U = (1 << N) - 1

    @cache
    def dfs(u, s):
        if s == U:
            return dist[u][0]

        res = float("inf")
        for v in range(N):
            if s & (1 << v):
                continue
            res = min(res, dist[u][v] + dfs(v, s | (1 << v)))
        return res

    print(dfs(0, 1))


if __name__ == "__main__":
    solve()
