"""
P4158 [SCOI2009] 粉刷匠
https://www.luogu.com.cn/problem/P4158
狀態機DP + 分組背包DP

Python TLE, C++ AC
"""
import sys
it = iter(sys.stdin.read().splitlines())
input = lambda: next(it)

def solve():
    N, M, T = map(int, input().split())
    # f[t] 表示粉刷 t 次時，能獲得的最大價值
    f = [0] * (T + 1)
    for _ in range(N):
        s = input()
        # g[i][j][0/1/2] 表示考慮到字串的前 i 個字元，粉刷 j 次，最後一個粉刷成紅色/藍色/未粉刷時，能獲得的最大價值
        # g = [[[0, 0, 0] for _ in range(T + 1)] for _ in range(2)]
        # for i, ch in enumerate(s, 1):
        #     curr, prev = g[i & 1], g[(i - 1) & 1]
        #     for j in range(1, T + 1):
        #         curr[j][0] = max(prev[j][0], prev[j - 1][1], prev[j - 1][2]) + (ch == '0')
        #         curr[j][1] = max(prev[j - 1][0], prev[j][1], prev[j - 1][2]) + (ch == '1')
        #         curr[j][2] = max(prev[j][0], prev[j][1], prev[j][2])
        g = [[0, 0, 0] for _ in range(T + 1)]
        for i, ch in enumerate(s, 1):
            for j in range(T, 0, -1):
                a, b, c = g[j]
                g[j][0] = max(a, g[j - 1][1], g[j - 1][2]) + (ch == '0')
                g[j][1] = max(g[j - 1][0], b, g[j - 1][2]) + (ch == '1')
                g[j][2] = max(a, b, c)
        # 分組背包
        items = [(t, max(g[t])) for t in range(1, T + 1)]
        for j in range(T, -1, -1):
            for t, c in items:
                if j >= t:
                    # f[j] = max(f[j], f[j - t] + c)
                    if f[j - t] + c > f[j]:
                        f[j] = f[j - t] + c
    print(max(f))

if __name__ == "__main__":
    solve()