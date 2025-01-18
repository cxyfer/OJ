"""
考慮以下兩種 Case
1. a = b，則會產生 len(g[a]) 個連通分量
2. a != b，則會產生一條路徑。對於路徑上的每一點 u：
  - 如果 u 在路徑中，則會產生 len(g[u]) - 2 個連通分量
  - 如果 u 是路徑的端點，則會產生 len(g[u]) - 1 個連通分量
  由於路徑一定有兩個端點，因此可以皆視為 len(g[u]) - 2 ，最後再 + 2 即可。

對於 Case 1，直接取 max(len(g[u])) 即可，但其實也可以視為 Case 2 的特例。
對於 Case 2，則約等同求樹上最長直徑，使用樹形 DP 維護子樹中最大及次大鏈值即可。
"""
t = int(input())

for _ in range(t):
    n = int(input())
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(lambda x: int(x) - 1, input().split())
        g[u].append(v)
        g[v].append(u)

    ans = max(len(g[u]) for u in range(n))
    # 用 stack 模擬遞迴
    stk = [(0, -1, False)]  # (node, parent, flag)
    f = [0] * n
    while stk:
        u, fa, flag = stk.pop()
        if not flag:
            stk.append((u, fa, True))
            stk.extend((v, u, False) for v in g[u] if v != fa)
            continue
        cur = len(g[u]) - 2 # 當前節點值
        first = second = 0 # 維護最大及次大鏈值
        for v in g[u]:
            if v == fa:
                continue
            t = f[v]
            if t > first:
                first, second = t, first
            elif t > second:
                second = t
        ans = max(ans, first + second + cur + 2) # 更新答案
        f[u] = first + cur # 更新該子樹的最大鏈值
    print(ans)