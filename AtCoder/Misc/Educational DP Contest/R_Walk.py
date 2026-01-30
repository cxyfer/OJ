MOD = int(1e9 + 7)

class Matrix:
    def __init__(self, mat):
        self.mat = mat

    def __mul__(self, other):
        assert len(self.mat[0]) == len(other.mat)
        return Matrix([[sum(x * y for x, y in zip(row, col)) % MOD for col in zip(*other.mat)]
                for row in self.mat])
    
    def __pow__(self, k):
        assert len(self.mat) == len(self.mat[0])
        n = len(self.mat)
        res = Matrix([[int(i == j) for j in range(n)] for i in range(n)])
        base = self
        while k > 0:
            if k & 1:
                res *= base
            base *= base
            k >>= 1
        return res
    
    def __getitem__(self, i):
        return self.mat[i]

def solve():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    A = Matrix(A)
    Ak = A ** K
    ans = 0
    for row in Ak.mat:
        ans = (ans + sum(row)) % MOD
    print(ans)

if __name__ == '__main__':
    solve()
