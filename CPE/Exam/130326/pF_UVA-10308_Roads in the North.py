"""
    樹形 DP ，求直徑
"""
from collections import defaultdict

run = True
while run:
    g = defaultdict(list)
    while True:
        try:
            line = input()
            if line == "":
                break
            u, v, w = map(int, line.split())
            g[u].append((v, w))
            g[v].append((u, w))
        except EOFError:
            run = False
            break
    
    ans = 0
    def dfs(u, fa):
        global ans
        res1, res2 = 0, 0
        for v, w in g[u]:
            if v == fa:
                continue
            cur = w + dfs(v, u)
            if cur > res1:
                res2 = res1
                res1 = cur
            elif cur > res2:
                res2 = cur
        ans = max(ans, res1 + res2)
        return res1
    
    dfs(1, -1)
    print(ans)