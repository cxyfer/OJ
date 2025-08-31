import sys
input = lambda: sys.stdin.readline().strip()

def solve():
    n, q = map(int, input().split())
    A = list(map(lambda x: int(x) - 1, input().split()))

    m = n.bit_length()
    # pa[u][i] 表示 u 的第 2^i 個祖先
    pa = [[-1] * m for _ in range(n)]
    for u, fa in enumerate(A, 1):
        pa[u][0] = fa

    # 用倍增法更新 pa
    for i in range(m - 1):
        for u in range(n):
            if pa[u][i] != -1:
                pa[u][i + 1] = pa[pa[u][i]][i]

    for _ in range(q):
        u, k = map(int, input().split())
        u -= 1
        while k and u != -1:
            lb = k & -k
            u = pa[u][lb.bit_length() - 1]
            k &= k - 1
        print(u + 1 if u != -1 else -1)
    return

if __name__ == "__main__":
    solve()