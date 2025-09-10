"""
P1064 [NOIP 2006 提高组] 金明的预算方案
https://www.luogu.com.cn/problem/P1064
背包DP模板題：分組背包

由於有附件跟主件依賴關係，可以看作是在每個主件分組內做分組背包。
https://oi-wiki.org/dp/knapsack/#%E6%9C%89%E4%BE%9D%E8%B5%96%E7%9A%84%E8%83%8C%E5%8C%85
"""
def solve():
    W, n = map(int, input().split())
    groups = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        v, p, q = map(int, input().split())
        g = i if q == 0 else q
        groups[g].append((v, p, i))

    f = [0] * (W + 1)
    for i, g in enumerate(groups):
        if len(g) == 0:
            continue
        g.sort(key=lambda x: x[2] == i, reverse=True)
        v0, p0, _ = g[0]
        items = [(v0, v0 * p0)]
        for v, p, _ in g[1:]:
            items.append((v0 + v, v0 * p0 + v * p))
        if len(g) == 3:
            items.append((sum(v for v, _, _ in g), sum(v * p for v, p, _ in g)))
        for j in range(W, -1, -1):
            for v, c in items:
                if j >= v:
                    f[j] = max(f[j], f[j - v] + c)
    print(f[W])

if __name__ == "__main__":
    solve()