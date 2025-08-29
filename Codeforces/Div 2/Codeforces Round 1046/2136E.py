from collections import deque
MOD = 998244353

def solve():
    n, m, V = map(int, input().split())
    A = list(map(int, input().split()))
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(lambda x: int(x) - 1, input().split())
        g[u].append(v)
        g[v].append(u)

    # 1. Find bridges (cut edges) by Tarjan's algorithm
    dfn = [-1] * n
    low = [-1] * n
    time = 0
    bridges = set()
    def dfs(u, fa):
        nonlocal time
    #     dfn[u] = low[u] = time
    #     time += 1
    #     for v in g[u]:
    #         if v == fa:
    #             continue
    #         if dfn[v] != -1:  # back edge
    #             low[u] = min(low[u], dfn[v])
    #         else:
    #             dfs(v, u)
    #             low[u] = min(low[u], low[v])
    #             if low[v] > dfn[u]:
    #                 bridges.add((min(u, v), max(u, v)))
        st = [(0, -1, 0)]
        while st:
            u, fa, i = st.pop()
            if i == 0:
                dfn[u] = low[u] = time
                time += 1
            if i < len(g[u]):
                v = g[u][i]
                st.append((u, fa, i + 1))
                if v == fa:
                    continue
                if dfn[v] != -1:  # back edge
                    low[u] = min(low[u], dfn[v])
                else:
                    st.append((v, u, 0))
            else:
                low[fa] = min(low[fa], low[u])
                if low[u] > dfn[fa]:
                    bridges.add((min(u, fa), max(u, fa)))
    dfs(0, -1)

    # 2. Find BCCs (biconnected components) by DFS
    comp = [-1] * n
    idx = 0
    def dfs2(u):
        # comp[u] = idx
        # for v in g[u]:
        #     if comp[v] != -1 or (min(u, v), max(u, v)) in bridges:
        #         continue
        #     dfs2(v)
        st = [(u, 0)]
        while st:
            u, i = st.pop()
            if i == 0:
                comp[u] = idx
            if i < len(g[u]):
                v = g[u][i]
                st.append((u, i + 1))
                if comp[v] != -1 or (min(u, v), max(u, v)) in bridges:
                    continue
                st.append((v, 0))

    for u in range(n):
        if comp[u] != -1:
            continue
        dfs2(u)
        idx += 1
    
    bccs = [[] for _ in range(idx)]
    for i in range(n):
        bccs[comp[i]].append(i)

    # 3. Process each BCC
    ans = 1

    color = [-1] * n
    def bipartite(u):
        q = deque([(u, 0)])
        color[u] = 0
        while q:
            u, c = q.popleft()
            for v in g[u]:
                if (min(u, v), max(u, v)) in bridges:
                    continue
                if color[v] == -1:
                    color[v] = c ^ 1
                    q.append((v, c ^ 1))
                elif color[v] == c:
                    return False
        return True
    
    for bcc in bccs:
        # a. Check consistency of weights and determine common weight
        weight = -1
        for u in bcc:
            if A[u] == -1:
                continue
            if weight != -1 and A[u] != weight:
                print(0)
                return
            weight = A[u]

        # b. Check for odd cycles (bipartite coloring)
        is_bipartite = bipartite(bcc[0])

        # c. Calculate the number of ways
        if not is_bipartite:  # odd cycle
            if weight != -1 and weight != 0:
                print(0)
                return
        elif weight == -1:  # all weights are unknown, can take any common value
            ans = (ans * V) % MOD
        else:  # all weights are known, only one value
            pass
    print(ans)

t = int(input())
for _ in range(t):
    solve()