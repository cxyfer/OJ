"""
【华为】20230412_3_获取最多食物
https://niumacode.com/problem/P1537
"""

n = int(input())

g = [[] for _ in range(n)]
W = [0] * n
root = -1
for _ in range(n):
    v, u, w = map(int, input().split())
    W[v] = w
    if u != -1:
        g[u].append(v)
    else:
        root = v

ans = 0
def dfs(u, fa):
    global ans
    res = 0
    for v in g[u]:
        if v == fa: continue
        res = max(res, dfs(v, u))
    ans = max(ans, res + W[u])
    return res + W[u]

dfs(root, -1)
print(ans)