"""
    DFS
    是問 l 次推倒後，總共有幾個骨牌會被推倒
    
    AC: UVA, CPE, ZeroJudge
"""
t = int(input())

def dfs(u):
    visited[u] = True
    res = 1 # u 倒下
    for v in g[u]:
        if not visited[v]: # v 未倒下
            res += dfs(v)
    return res

for _ in range(t):
    n, m, l = map(int, input().split())
    g = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        g[u-1].append(v-1)

    ans = 0
    visited = [False] * n
    for _ in range(l):
        z = int(input())
        if not visited[z-1]:
            ans += dfs(z-1)
    print(ans)