from collections import deque

MOD = 998244353

t = int(input().strip())
for _ in range(t):
    N, Q = map(int, input().split())
    g = [[] for _ in range(N)]
    deg = [0] * N
    for __ in range(N - 1):
        u, v = map(lambda x: int(x) - 1, input().split())
        g[u].append(v)
        g[v].append(u)
        deg[u] += 1
        deg[v] += 1

    fa = [0] * N
    q = deque([0])
    order = [] # Level order
    vis = [False] * N
    vis[0] = True
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            if vis[v]:
                continue
            vis[v] = True
            fa[v] = u
            q.append(v)
    
    queries = []
    max_k = 0
    for __ in range(Q):
        vi, ki = map(int, input().split())
        queries.append((vi - 1, ki))
        max_k = max(max_k, ki)

    # f_o[v][k] 表示從節點 v 開始，這一步是奇數步，且剩餘硬幣數為 k 時，達到根節點的期望步數。
    # f_e[v][k] 表示從節點 v 開始，這一步是偶數步，且剩餘硬幣數為 k 時，達到根節點的期望步數。
    f_o = [[0] * (max_k + 1) for _ in range(N)]
    f_e = [[0] * (max_k + 1) for _ in range(N)]

    for k in range(0, max_k + 1):
        for u in order:
            if u == 0:
                f_o[u][k] = 0
                f_e[u][k] = 0
                continue
            pu = fa[u]

            # 奇數步：只能往上走
            f_o[u][k] = 1 + f_e[pu][k]

            # 偶數步：
            # 1. 可以支付 1 個代價往上走
            opt1 = 1 + f_o[pu][k - 1]
            # 2. 不支付代價，隨機往相鄰的節點走
            opt2 = 2 * deg[u] - 1 + f_o[pu][k]
            # 若 k >= 1，則可以支付代價，兩者取最小值
            f_e[u][k] = min(opt1, opt2) if k >= 1 else opt2

    for vi, ki in queries:
        print(f_o[vi][ki] % MOD)