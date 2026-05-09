import sys

sys.setrecursionlimit(int(3e5))


def main():
    n = int(input())
    g = [[] for _ in range(n)]

    for _ in range(n - 1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    pa = [-1] * n
    sz = [1] * n

    def dfs(u, fa):
        pa[u] = fa
        for v in g[u]:
            if v == fa:
                continue
            dfs(v, u)
            sz[u] += sz[v]

    dfs(0, -1)

    # g(1)：路徑包含點 0 的數量
    # 全部路徑數量是 N * (N + 1) // 2
    # 不經過 0 的路徑，一定完全在 0 的某個兒子子樹中
    ans = n * (n + 1) // 2
    for v in g[0]:
        ans -= sz[v] * (sz[v] + 1) // 2

    # vis[x] 表示 x 是否已經在目前維護的路徑上
    vis = [False] * n
    vis[0] = True

    L = R = 0  # 目前維護的最小路徑兩端點
    for x in range(1, n):
        # 如果 x 已經在目前路徑上，新增 x 不會改變條件
        if vis[x]:
            ans += sz[L] * sz[R]
            continue

        # 從 x 往上跳，直到遇到目前路徑上的點 y
        vis[x] = True
        v = x
        while not vis[pa[v]]:
            vis[pa[v]] = True
            v = pa[v]
        y = pa[v]

        # 如果 y 不是目前路徑端點，表示接到路徑中間，會產生分叉
        # 之後不可能存在包含所有 0..x 的簡單路徑
        if y != L and y != R:
            break

        # y 是端點，可以把端點延伸成 x
        if y == L:
            L = x
        else:
            R = x

        # 如果是從根 0 往某個方向延伸，
        # 那麼根這一側能選的端點數量要扣掉 child 這棵子樹
        if y == 0:
            sz[0] -= sz[v]

        # 目前路徑端點是 L, R
        # 可以選的總路徑數量就是兩側大小相乘
        ans += sz[L] * sz[R]

    print(ans)


if __name__ == "__main__":
    main()
