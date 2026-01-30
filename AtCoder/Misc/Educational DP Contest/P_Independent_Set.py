from collections import deque

MOD = int(1e9 + 7)

def solve():
    N = int(input())
    g = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(lambda x: int(x) - 1, input().split())
        g[u].append(v)
        g[v].append(u)

    # @cache
    # def dfs(u: int, fa: int) -> list[int]:
    #     res = [1, 1]
    #     for v in g[u]:
    #         if v == fa:
    #             continue
    #         white, black = dfs(v, u)
    #         res[1] = (res[1] * white) % MOD
    #         res[0] = (res[0] * (white + black)) % MOD
    #     return res
    # print(sum(dfs(0, -1)) % MOD)

    fa = [-1] * N
    order = []
    q = deque([0])
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            if v == fa[u]:
                continue
            fa[v] = u
            q.append(v)

    # f[u][0/1]: u 塗白/黑色的方案數
    f = [[1, 1] for _ in range(N)]
    for u in reversed(order):
        for v in g[u]:
            if v == fa[u]:
                continue
            f[u][1] = (f[u][1] * f[v][0]) % MOD
            f[u][0] = (f[u][0] * (f[v][0] + f[v][1])) % MOD
    print(sum(f[0]) % MOD)

if __name__ == "__main__":
    solve()