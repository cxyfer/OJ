"""
J. MST Problem
https://ac.nowcoder.com/acm/contest/120561/J

Boruvka's algorithm
"""
class UnionFind:
    __slots__ = ['n', 'pa', 'sz', 'cnt']

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
    n, m = map(int, input().split())
    A = list(map(int, input().split()))

    ban = [set() for _ in range(n)]
    for _ in range(m):
        u, v = map(lambda x: int(x) - 1, input().split())
        ban[u].add(v)
        ban[v].add(u)
 
    nodes = sorted(enumerate(A), key=lambda x: x[1])
    mn_val = min(A)

    ans = 0
    uf = UnionFind(n)

    # 做 log(n) 次 Boruvka
    active = True
    while uf.cnt > 1 and active:
        active = False

        # 將節點按連通分量分組
        comps = [[] for _ in range(n)]
        for u in range(n):
            comps[uf.find(u)].append(u)

        # 對於每個連通分量，尋找最小出邊
        records = []
        for i, comp in enumerate(comps):
            if not comp:
                continue

            # 初始化最小出邊
            edge = (float('inf'), -1, -1)

            # 使用 iterator 維護不屬於當前連通分量的節點 
            source = (v for v, _ in nodes if uf.find(v) != i)
            candidates = []  # 緩存
            # 使用 generator 先產出緩存中的節點，如果需要更多則從 source 中獲取
            def get_candidates():
                yield from candidates
                for v in source:
                    candidates.append(v)
                    yield v

            for u in comp:
                # 剪枝，如果 u 的權重加上最小權重已經超過當前找到的最小值，則 u 無法貢獻更優解
                if A[u] + mn_val >= edge[0]:
                    continue
                # 找到以 u 為起點的最小出邊
                for v in get_candidates():
                    if v in ban[u]:
                        continue
                    edge = min(edge, (A[u] + A[v], u, v))
                    break

            if edge[1] != -1:
                records.append(edge)

        # 合併找到的邊，注意需要當這輪結束時，才能改變 DSU 的狀態
        for w, u, v in records:
            if uf.union(u, v):
                ans += w
                active = True

    print(ans if uf.cnt == 1 else -1)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()