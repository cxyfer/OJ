from collections import deque


def solve():
    n = int(input())
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(lambda x: int(x) - 1, input().split())
        g[u].append(v)
        g[v].append(u)

    def bfs(st: int) -> list[int]:
        dist = [float("inf")] * n
        dist[st] = 0
        q = deque([st])
        while q:
            u = q.popleft()
            for v in g[u]:
                if dist[v] == float("inf"):
                    dist[v] = dist[u] + 1
                    q.append(v)
        return dist

    # BFS/DFS 求直徑，但需要取編號較大的點
    dist = bfs(0)
    x = -1
    for u in range(n):
        if dist[u] >= dist[x]:
            x = u
    distx = bfs(x)
    y = -1
    for u in range(n):
        if distx[u] >= distx[y]:
            y = u
    disty = bfs(y)

    # 確保 x 的編號比 y 的編號大
    if x < y:
        x, y = y, x
        distx, disty = disty, distx

    ans = []
    for u in range(n):
        d1 = distx[u]
        d2 = disty[u]
        # 距離 u 最遠的點一定是直徑上的端點之一
        ans.append(x + 1 if d1 >= d2 else y + 1)
    print(*ans, sep="\n")


if __name__ == "__main__":
    solve()
