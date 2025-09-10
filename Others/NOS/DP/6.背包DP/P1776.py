"""
P1776 宝物筛选
https://www.luogu.com.cn/problem/P1776
背包DP模板題：多重背包

這裡提供一個有別於二進制拆分的拆分方式，即 330. Patching Array 的貪心思路。
設當前可以構造出區間 [0, s] 中的任何數，初始化為 s = 0，則下一個需要構造的數為 s + 1。
考慮新增的數字 x，則可以產生新的區間 [x, s + x]，
當 x = s + 1 時，新增的區間和原本的區間洽連續，即可以讓區間擴展到 [0, s + x]。
故貪心的選擇 s + 1 作為新增的數，但注意我們構造的數的總和只能是 m，因此最後一次選擇的數字可能會小於 s + 1。
"""
def solve():
    n, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]

    items = []
    for v, w, m in A:
        s = 0  # 當前可以構造出 [0, s] 中的數
        tot = 0  # 當前已經構造出的數的總和
        while s < m:
            x = min(s + 1, m - tot)
            tot += x
            items.append((v * x, w * x))
            s += x

    f = [0] * (W + 1)
    for v, w in items:
        for j in range(W, w - 1, -1):
            f[j] = max(f[j], f[j - w] + v)
    print(f[W])

if __name__ == "__main__":
    solve()