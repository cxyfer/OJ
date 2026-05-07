class SparseTable:
    def __init__(self, data, func):
        n = len(data)
        self.data = data
        self.merge = func
        k = n.bit_length() - 1

        st = [[None] * (k + 1) for _ in range(n)]
        for i in range(n):
            st[i][0] = data[i]
        for j in range(1, k + 1):
            for i in range(n):
                st[i][j] = func(st[i][j - 1], st[min(n - 1, i + (1 << (j - 1)))][j - 1])
        self.st = st

    def query(self, L, R):  # 0-indexed
        k = (R - L + 1).bit_length() - 1
        return self.merge(self.st[L][k], self.st[R - (1 << k) + 1][k])


def solve():
    n, q = map(int, input().split())
    A = [int(input()) for _ in range(n)]

    st_mx = SparseTable(A, max)
    st_mn = SparseTable(A, min)

    for _ in range(q):
        l, r = map(lambda x: int(x) - 1, input().split())
        print(st_mx.query(l, r) - st_mn.query(l, r))


if __name__ == "__main__":
    solve()
