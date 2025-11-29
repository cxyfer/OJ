"""
很好的題目，可惜卡常。
Python 版本留做理解題目用。
"""
import sys
import math
from itertools import accumulate

it = iter(sys.stdin.read().splitlines())
def input():
    return next(it)

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

def solve():
    n = int(input())
    S = list(map(lambda c: ord(c) - ord('a'), input()))
    A = list(map(int, input().split()))

    # pre[c][i] 表示第 i 個位置之前最後一個出現字母 c 的位置
    pre = [[0] * (n + 1) for _ in range(26)]
    for i, c in enumerate(S, start=1):
        for j in range(26):
            pre[j][i] = i if c == j else pre[j][i - 1]

    # 前綴異或和維護區間內哪些字母出現了奇數次
    xor = list(accumulate(S, func=lambda x, c: x ^ (1 << c), initial=0))
    # ST 表維護區間內的字母出現情況
    vis = [0] + list(map(lambda c: 1 << c, S))
    st = SparseTable(vis, lambda x, y: x | y)

    q = int(input())
    ans = []
    for _ in range(q):
        op, *args = map(int, input().split())
        if op == 1:
            x, y = args
            A[x - 1] = y
        elif op == 2:
            l, r = args
            res = 0
            for c in range(26):
                p = pre[c][r]
                if p < l:
                    continue
                msk1 = xor[p - 1] ^ xor[l - 1]
                msk2 = st.query(p, r)
                if msk1 & msk2 == 0:
                    res += A[p - 1]
            ans.append(res)
    print(*ans, sep='\n')

if __name__ == "__main__":
    solve()