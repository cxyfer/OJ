"""
SparseTable 模板

可以用來解決可重複貢獻的區間查詢問題，例如區間最大值、區間最小值、區間按位或、區間按位與、區間GCD等。
注意對於區間和這種不可重複貢獻的問題，不能使用SparseTable。
"""

import math

class SparseTable:
    def __init__(self, data, merge_func):
        n = len(data)
        self.data = data
        self.merge = merge_func
        self.max_log = math.floor(math.log2(n)) if n > 0 else 0
        self.st = [[None] * (self.max_log + 1) for _ in range(n)]
        for i in range(n):
            self.st[i][0] = data[i]
        
        for j in range(1, self.max_log + 1):
            for i in range(n):
                self.st[i][j] = self.merge(self.st[i][j - 1], self.st[min(n - 1, i + (1 << (j - 1)))][j - 1])
    
    def query(self, L, R):  # 0-indexed
        k = math.floor(math.log2(R - L + 1))
        return self.merge(self.st[L][k], self.st[R - (1 << k) + 1][k])
    
# Example of usage
A = list(range(1, 11))
st_mx = SparseTable(A, max)
print(st_mx.query(0, 9))
print(st_mx.query(0, 4))
print(st_mx.query(5, 9))