import math

class SparseTable:
    def __init__(self, data, merge_func):
        self.n = len(data)
        self.data = data
        self.merge = merge_func
        self.max_log = math.floor(math.log2(self.n)) if self.n > 0 else 0
        self.st = [[None] * (self.max_log + 1) for _ in range(self.n)]
        for i in range(self.n):
            self.st[i][0] = data[i]
        
        for j in range(1, self.max_log + 1):
            for i in range(self.n):
                self.st[i][j] = self.merge(self.st[i][j - 1], self.st[min(n - 1, i + (1 << (j - 1)))][j - 1])
    
    def query(self, L, R):
        k = math.floor(math.log2(R - L + 1))
        return self.merge(self.st[L][k], self.st[R - (1 << k) + 1][k])
    
n, q = map(int, input().split())
A = [int(input()) for _ in range(n)]

st_mx = SparseTable(A, max)
st_mn = SparseTable(A, min)

for _ in range(q):
    l, r = map(lambda x : int(x) - 1, input().split())
    print(st_mx.query(l, r) - st_mn.query(l, r))