""" Tree DP
    可以當作無向樹來處理，這樣可以以任意一個點當作根節點。
"""

# def dfs(u, fa):
#     global ans
#     p = 1 # need
#     q = marbles[u] # have
#     for v in g[u]:
#         if v == fa:
#             continue
#         p2, q2 = dfs(v, u)
#         p += p2
#         q += q2
#     ans += abs(p - q)
#     return p, q

def dfs(u, fa): # 正數表示多餘，負數表示缺少
    global ans
    res = marbles[u] - 1
    for v in g[u]:
        if v == fa:
            continue
        res_v = dfs(v, u)
        ans += abs(res_v)
        res += res_v
    return res

while True:
    n = int(input())
    if n == 0:
        break
    g = [[] for _ in range(n + 1)]
    marbles = [0] * (n + 1)

    for _ in range(n):
        u, m, d, *nodes = map(int, input().split())
        marbles[u] = m
        for v in nodes: # 建立無向樹
            g[u].append(v)
            g[v].append(u)
    
    ans = 0
    dfs(1, 0) # 以任意點當作根節點皆可
    print(ans)
