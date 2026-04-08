class UnionFind:
    __slots__ = ["n", "pa", "sz", "cnt"]

    def __init__(self, n: int):
        self.n = n
        self.pa = list(range(n))  # 父節點
        self.sz = [1] * n  # 連通分量大小
        self.cnt = n  # 連通分量數量

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
        self.cnt -= 1
        return True


def solve():
    n, m, k = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]

    """使用 WQS Binary Search (Aliens Trick) 計算當使用恰好 k 條白色邊時的最小成本"""

    def check(c: int):
        
        edges.sort(key=lambda x: (x[2] + (c if x[3] == 0 else 0), -x[3]))  # 相同成本時，優先選擇黑色邊

        cost = cnt = 0
        uf = UnionFind(n)
        for u, v, w, col in edges:
            if uf.union(u, v):
                # 將白色邊的成本加上 c，黑色邊的成本不變
                cost += w + (c if col == 0 else 0)
                cnt += (col == 0)
                if uf.cnt == 1:
                    break
        return cost, cnt

    # 從選 k - 1 個增加到 k 個需要 k * mx 的成本
    mx = max(w for _, _, w, _ in edges)
    left, right = -mx, mx
    while left <= right:
        mid = (left + right) // 2
        _, cnt = check(mid)
        if cnt <= k:  # 要多選，成本需要降低
            right = mid - 1
        else:  # 要少選，成本需要升高
            left = mid + 1

    print(check(left)[0] - k * left)


if __name__ == "__main__":
    solve()
