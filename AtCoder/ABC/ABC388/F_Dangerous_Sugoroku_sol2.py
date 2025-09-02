N, M, A, B = map(int, input().split())
intervals = [tuple(map(int, input().split())) for _ in range(M)]

class Matrix:
    def __init__(self, r, c, mat=None):
        self.r = r
        self.c = c
        self.mat = mat or [0] * r

    def __mul__(self, other):
        res = [0] * len(self.mat)
        # for i, row in enumerate(self.mat):
        #     for k in range(other.r):
        #         if row & (1 << k):
        #             res[i] |= other.mat[k]
        for i, row in enumerate(self.mat):
            while row:
                lb = row & -row
                k = lb.bit_length() - 1
                res[i] |= other.mat[k]
                row ^= lb
        return Matrix(self.r, other.c, res)
    
    def __getitem__(self, key):
        i, j = key
        return (self.mat[i] >> j) & 1
    
    def __setitem__(self, key, value):
        i, j = key
        if value:
            self.mat[i] |= (1 << j)
        else:
            self.mat[i] &= ~(1 << j)
    
MG = Matrix(B, B)  # Good
for i in range(A - 1, B):
    MG[0, i] = 1
for i in range(1, B):
    MG[i, i - 1] = 1

MB = Matrix(B, B)  # Bad
for i in range(1, B):
    MB[i, i - 1] = 1

pow_MG, pow_MB = [0] * 41, [0] * 41
pow_MG[0], pow_MB[0] = MG, MB
for i in range(1, 41):
    pow_MG[i] = pow_MG[i - 1] * pow_MG[i - 1]
    pow_MB[i] = pow_MB[i - 1] * pow_MB[i - 1]

identity = Matrix(B, B)
for i in range(B):
    identity[i, i] = 1

def pow(x, k, pow_mat):
    """
    根據矩陣快速冪，可以把 MB^k 表示成 MB^(2^i) 的乘積。
    因此在預先處理完 MB^(2^i) 的矩陣後，需要計算若干個 (B x B) 的矩陣相乘後再乘以一個 (B x 1) 的矩陣。
    
    但注意這裡有個小技巧：
    兩個 (B x B) 的矩陣相乘需要 O(B^3) 的時間；
    而 (B x B) 的矩陣乘以 (B x 1) 的矩陣只需要 O(B^2) 的時間。

    因此我們應該由後往前計算，這樣可以減少計算的次數。
    如此便可以在 O(B^2 log k) 的時間內計算出 MB^k * x 。

    不過如果用狀態壓縮 + 位運算，則不管是計算上述兩者中的哪一個，都只需要 O(B^2) 的時間。
    """
    res = x
    for i in range(41):
        if k & (1 << i):
            res = pow_mat[i] * res
    return res
    # res = identity
    # for i in range(41):
    #     if k & (1 << i):
    #         res = pow_mat[i] * res
    # return res * x

cur = 1
# m = [[0] for _ in range(B)]
m = [0] * B
m[0] = 1
x = Matrix(B, 1, m)
for (L, R) in intervals:
    # (cur, L-1] is good
    x = pow(x, L - 1 - cur, pow_MG)
    # (L-1, R] is bad
    x = pow(x, R - L + 1, pow_MB)
    cur = R

# (cur, N] is good
x = pow(x, N - cur, pow_MG)
print("Yes" if x[0, 0] else "No")