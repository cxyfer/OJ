from collections import deque


def solve():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    ind = [0] * n
    for _ in range(m):
        u, v = map(lambda x: int(x) - 1, input().split())
        g[u].append(v)
        g[v].append(u)
        ind[u] += 1
        ind[v] += 1

    q = deque()
    for u in range(n):
        if ind[u] == 1:
            q.append(u)

    ans = 0
    while q and any(ind[u] == 1 for u in q):
        for _ in range(len(q)):
            u = q.popleft()
            if ind[u] != 1:
                continue
            for v in g[u]:
                ind[v] -= 1
                if ind[v] == 1:
                    q.append(v)
        ans += 1
    print(ans)


if __name__ == "__main__":
    solve()
