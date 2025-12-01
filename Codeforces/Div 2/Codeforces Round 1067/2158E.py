"""
圖論 + DSU

題意為求有多少個可以被視為「山谷」的區域，這個區域內的數字皆相同，且周圍不存在比它更小的數字。

首先考慮不帶修改的情況要怎麼做。
直覺可能會將低和高的格子連接起來，但這樣顯然是錯的，會錯誤的將多個山谷連接起來。
正確的做法是將相鄰的相同值的格子合併，並維護周圍是否有更小數字的標記。
如果周圍沒有更小數字的話，那這個合併的連通分量就是一個「山谷」，需計入答案。

接著考慮帶修改的情況，以及要如何計算答案。
DSU 是很難拆分節點的，但我們可以將修改後的數字視為一個新的節點，並在這個新節點上操作。
由於每次修改時，最多只會影響周圍以及自己本身的 5 個連通分量，因此可以先撤回這些連通分量對答案的貢獻，再重新計算。
"""
class UnionFind:
    __slots__ = ['n', 'pa', 'sz', 'val', 'flag']

    def __init__(self, n: int):
        self.n = n
        self.pa = list(range(n))  # 父節點
        self.sz = [1] * n  # 連通分量大小
        self.val = [0] * n  # 保存每個節點的數值
        self.flag = [1] * n  # 1 代表是「山谷」，也就是周圍不存在比它更小的節點

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
        self.flag[fx] = min(self.flag[fx], self.flag[fy])
        return True

def solve():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    
    q = int(input())
    uf = UnionFind(n * m + q + 5)

    # mp[r][c] 儲存格子 (r, c) 當前對應的節點編號
    mp = [[r * m + c for c in range(m)] for r in range(n)]
    
    def get_neighbors(r, c):
        if r > 0: yield r - 1, c
        if r + 1 < n: yield r + 1, c
        if c > 0: yield r, c - 1
        if c + 1 < m: yield r, c + 1
    
    for r, row in enumerate(grid):
        for c, x in enumerate(row):
            uf.val[r * m + c] = x
            for nr, nc in get_neighbors(r, c):
                if grid[nr][nc] == x:  # 合併相同值的節點
                    uf.union(r * m + c, nr * m + nc)
                elif grid[nr][nc] < x:  # 如果周圍有比它更小的節點，則這個連通分量不會是「山谷」
                    uf.flag[uf.find(r * m + c)] = 0  # 注意這裡需要使用 find 找到根節點

    # 計算初始時有幾個「山谷」
    ans = 0
    for r, row in enumerate(grid):
        for c, x in enumerate(row):
            u = r * m + c
            if uf.find(u) == u:
                ans += uf.flag[u]
    print(ans)
    
    # 處理查詢
    idx = n * m  # 下一個可用的節點編號
    for _ in range(q):
        r, c, x = map(int, input().split())
        r, c = r - 1, c - 1
        x = uf.val[mp[r][c]] - x

        # 1. 找到會受到影響的連通分量 (最多 5 個)
        roots = set(uf.find(mp[nr][nc]) for nr, nc in get_neighbors(r, c))
        roots.add(uf.find(mp[r][c]))

        # 2. 減去這些連通分量原本對答案的貢獻，並更新這些連通分量的狀態
        for v in roots:
            ans -= uf.flag[v]
            if uf.val[v] > x:  # 這個連通分量不會是「山谷」了
                uf.flag[v] = 0
        
        # 3. 創建新節點，維護新節點的狀態以及與周圍節點的連通性
        u = idx
        idx += 1
        mp[r][c] = u
        uf.val[u] = x
        uf.flag[u] = all(uf.val[mp[nr][nc]] >= x for nr, nc in get_neighbors(r, c))
        for nr, nc in get_neighbors(r, c):
            if uf.val[mp[nr][nc]] == x:  # 合併相同值的節點
                uf.union(u, mp[nr][nc])

        # 4. 重新加回這些連通分量對答案的貢獻
        roots = set(uf.find(mp[nr][nc]) for nr, nc in get_neighbors(r, c))
        roots.add(uf.find(mp[r][c]))
        for v in roots:
            ans += uf.flag[v]

        print(ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()