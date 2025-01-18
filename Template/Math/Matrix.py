MOD = 10 ** 9 + 7

class Matrix:
    def __init__(self, mat):
        self.mat = mat

    def __mul__(self, other):
        assert len(self.mat[0]) == len(other.mat)
        p, q, r = len(self.mat), len(other.mat), len(other.mat[0])
        res = [[0] * r for _ in range(p)]
        for k in range(q):
            for i in range(p):
                for j in range(r):
                    res[i][j] += self.mat[i][k] * other.mat[k][j]
                    res[i][j] %= MOD
        return Matrix(res)
    
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
    
    def __getitem__(self, key):
        i, j = key
        return self.mat[i][j]
    
    def __setitem__(self, key, value):
        i, j = key
        self.mat[i][j] = value

    def __str__(self):
        return "\n".join(map(lambda x: " ".join(map(str, x)), self.mat))

if __name__ == "__main__":
    mat = Matrix([[1, 1], [1, 0]])
    x = Matrix([[1], [0]])
    print(mat ** 10 * x)

