import sys
input = lambda: sys.stdin.readline().strip()
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)

def solve():
    n, m = map(int, input().split())
    
    edges = []
    g = [[] for _ in range(n)]
    for eid in range(n - 1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        edges.append([u, v, w])
        g[u].append((v, eid))
        g[v].append((u, eid))
    
    # DSU
    pa = list(range(n))
    def find(x):
        while pa[x] != x:
            pa[x] = pa[pa[x]]
            x = pa[x]
        return x
    
    to_fa = [(-1, -1)] * n  # (fa, eid)
    dep = [0] * n
    def dfs(u):
        # for v, eid in g[u]:
        #     if v == to_fa[u][0]:
        #         continue
        #     if edges[eid][2] == 1:
        #         pa[v] = find(u)
        #     to_fa[v] = (u, eid)
        #     dep[v] = dep[u] + 1
        #     dfs(v)
        st = [u]
        while st:
            u = st.pop()
            for v, eid in g[u]:
                if v == to_fa[u][0]:
                    continue
                if edges[eid][2] == 1:
                    pa[v] = find(u)
                to_fa[v] = (u, eid)
                dep[v] = dep[u] + 1
                st.append(v)
    dfs(0)

    ans = []
    for _ in range(m):
        op, *args = map(int, input().split())
        if op == 1:
            a, b, y = args
            a -= 1
            b -= 1
            a, b = find(a), find(b)
            while y > 0 and a != b:
                if dep[a] > dep[b]:
                    a, b = b, a
                fa, eid = to_fa[b]
                y //= edges[eid][2]
                # Python 需要在查詢時才合併，否則會 TLE
                if edges[eid][2] == 1:
                    pa[b] = find(fa)
                b = find(fa)
            ans.append(y)
        else:
            eid, c = args
            eid -= 1
            edges[eid][2] = c
            # 其他語言可以在更新時就合併
    
    print(*ans, sep='\n')

if __name__ == "__main__":
    solve()