import bisect

class BIT:
    def __init__(self, size):
        self.N = size
        self.tree = [0] * (self.N + 2)

    def add(self, idx, val=1):
        while idx <= self.N:
            self.tree[idx] += val
            idx += idx & -idx

    def query(self, idx):
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res

    def range_query(self, l, r):
        return self.query(r) - self.query(l - 1)
    
t = int(input())
for _ in range(t):
    N, K = map(int, input().split())
    X = sorted(map(int, input().split()))
    restrictions = []
    for _ in range(K):
        l, r, t = map(int, input().split())
        restrictions.append((l, r, t))
    restrictions.sort(key=lambda x: x[1])

    bit = BIT(N)
    pa = [i for i in range(N + 2)]  # 左邊第一個未種的樹(包含自己)
    def find(x):
        if x < 1:
            return x
        if pa[x] != x:
            pa[x] = find(pa[x])
        return pa[x]
    
    for l_val, r_val, t_i in restrictions:
        L = bisect.bisect_left(X, l_val) + 1  # 1-indexed
        R = bisect.bisect_right(X, r_val)     # 1-indexed
        need = t_i - bit.range_query(L, R)
        if need <= 0:
            continue
        for _ in range(need):
            pos = find(R)
            bit.add(pos)  # 種樹
            pa[pos] = pos - 1  # 更新左邊第一個未種的樹

    print(N - bit.query(N))