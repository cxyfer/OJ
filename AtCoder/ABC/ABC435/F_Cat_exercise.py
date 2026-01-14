import sys
sys.setrecursionlimit(int(2e5 + 5))

class SparseTable:
    def __init__(self, data, merge_func):
        n = len(data)
        self.data = data
        self.merge = merge_func
        k = n.bit_length() - 1
        self.st = [[None] * (k + 1) for _ in range(n)]
        for i in range(n):
            self.st[i][0] = data[i]
        
        for j in range(1, k + 1):
            for i in range(n):
                self.st[i][j] = self.merge(self.st[i][j - 1], self.st[min(n - 1, i + (1 << (j - 1)))][j - 1])
    
    def query(self, L, R):  # 0-indexed
        k = (R - L + 1).bit_length() - 1
        return self.merge(self.st[L][k], self.st[R - (1 << k) + 1][k])

fmax = lambda a, b: a if a > b else b

def solve():
    n = int(input())
    A = list(map(int, input().split()))

    mp = {x : i for i, x in enumerate(A)}
    st = SparseTable(A, fmax)

    def dfs(l: int, r: int, pos: int) -> int:
        if l >= r:
            return 0
        res = float('-inf')
        if l <= pos - 1:
            x = st.query(l, pos - 1)
            res = fmax(res, abs(pos - mp[x]) + dfs(l, pos - 1, mp[x]))
        if pos + 1 <= r:
            x = st.query(pos + 1, r)
            res = fmax(res, abs(pos - mp[x]) + dfs(pos + 1, r, mp[x]))
        return res

    print(dfs(0, n - 1, mp[n]))

if __name__ == "__main__":
    solve()