"""
P14362 [CSP-S 2025] 道路修复 / road（官方数据）
https://www.luogu.com.cn/problem/P14362

MST

給定一個 n 個城市 k 個鄉鎮的圖，城市之間有 m 條道路，
且每個鄉鎮都和所有城市相連，但啟用鄉鎮需要額外的代價。
求使所有城市連通的最小代價。

注意到 k <= 10，這暗示我們可以二進位枚舉所有的鄉鎮狀態。
在原圖中只有 MST 上的邊需要考慮，因此我們可以先求出 MST，這樣可以把 m 減少到 n - 1

對於枚舉的狀態可以把啟用的鄉鎮相鄰的邊加入再求一次 MST，但瓶頸在每次都需要重新排序。
因此可以直接把所有邊都加入，然後只選擇啟用的鄉鎮相鄰的邊，這樣可以避免重新排序。

第一次MST需要 O(m log m) 的時間
排序 (n - 1) + kn 條邊需要 kn log kn 的時間
枚舉狀態需要 2^k 次，每次需要 O(kn) 的時間來計算當前狀態的 MST
總時間複雜度為 O(m log m + kn log kn + 2^k * kn)

Python 會被卡常數，同樣邏輯使用 C++ 實現可以 AC。
"""
class UnionFind:
    __slots__ = ['n', 'pa', 'sz']

    def __init__(self, n: int):
        self.n = n
        self.pa = list(range(n)) # 父節點
        self.sz = [1] * n # 連通分量大小

    def find(self, x: int) -> int:
        while self.pa[x] != x:
            self.pa[x] = self.pa[self.pa[x]]
            x = self.pa[x]
        return x

    def union(self, x: int, y: int) -> bool:
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False
        if self.sz[fx] < self.sz[fy]:
            fx, fy = fy, fx
        self.pa[fy] = fx
        self.sz[fx] += self.sz[fy]
        return True

def solve():
    n, m, k = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    edges.sort(key=lambda x: x[2])

    uf = UnionFind(n + 1)
    idx = 0
    for u, v, w in edges:
        if uf.union(u, v):
            edges[idx] = (u, v, w)
            idx += 1
            if idx == n - 1:
                break
    del edges[idx:]  # 保留 MST 上的邊
    ans = sum(w for _, _, w in edges)

    cost = [0] * (k + 1)
    for j in range(1, k + 1):
        c, *W = map(int, input().split())
        cost[j] = c
        for i, w in enumerate(W, start=1):
            edges.append((i, n + j, w))
    edges.sort(key=lambda x: x[2])

    for msk in range(1, 1 << k):
        cur = 0
        vis = [False] * (k + 1)
        for i in range(k):
            if msk & (1 << i):
                cur += cost[i + 1]
                vis[i + 1] = True

        uf = UnionFind(n + k + 1)
        idx = 0
        tgt = n + msk.bit_count() - 1
        for u, v, w in edges:
            if v > n and not vis[v - n]:
                continue
            if uf.union(u, v):
                cur += w
                idx += 1
                if idx == tgt:
                    break

        if cur < ans:
            ans = cur

    print(ans)

if __name__ == "__main__":
    solve()