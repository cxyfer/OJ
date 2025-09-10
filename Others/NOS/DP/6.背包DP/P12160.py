"""
P12160 [蓝桥杯 2025 省 Java B] 2 的幂
https://www.luogu.com.cn/problem/P12160
"""
def solve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    D = int(1e5 + 5).bit_length() - 1

    # f[i][j] 表示使前 i 個數字的乘積為 2^j 的倍數之最小代價
    f = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    f[0][0] = 0
    for i, x in enumerate(A, 1):
        f[i][0] = 0
        for j in range(1, k + 1):
            f[i][j] = f[i - 1][j]
            for d in range(1, min(D, j) + 1):
                y = 1 << d
                if x >= y:
                    r = x % y
                    w = 0 if r == 0 else (y - r if x - r + y <= int(1e5) else float('inf'))
                else:
                    w = y - x
                f[i][j] = min(f[i][j], f[i - 1][j - d] + w)
    print(f[n][k] if f[n][k] != float('inf') else -1)

if __name__ == "__main__":
    t = 1
    for _ in range(t):
        solve()