import sys
input = lambda: sys.stdin.readline().strip()
print = lambda val: sys.stdout.write(str(val) + "\n")

MOD = 10 ** 9 + 7

class Matrix:
    def __init__(self, mat):
        self.mat = mat

    def __mul__(self, other):
        p, r = len(self.mat), len(other.mat[0])

        other_t = list(zip(*other.mat))
        
        res = [[0] * r for _ in range(p)]
        for i in range(p):
            for j in range(r):
                res[i][j] = sum(a * b for a, b in zip(self.mat[i], other_t[j])) % MOD
        return Matrix(res)
    
    def __pow__(self, k):
        n = len(self.mat)
        res = Matrix([[int(i == j) for j in range(n)] for i in range(n)])
        base = self
        while k > 0:
            if k & 1:
                res *= base
            base *= base
            k >>= 1
        return res

n, k = map(int, input().split())
m = Matrix([list(map(int, input().split())) for _ in range(n)])
res = m ** k

for row in res.mat:
    print(' '.join(map(str, row)))