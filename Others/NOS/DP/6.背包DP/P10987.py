"""
P10987 [蓝桥杯 2023 国 Python A] 火车运输
https://www.luogu.com.cn/problem/P10987
背包DP模板題：二維DP
"""
def solve():
    N, A, B = map(int, input().split())
    X = list(map(int, input().split()))

    # f[s1][s2] 表示當前 A 車廂已經裝了 s1 重的鋼材時，B 車廂已經裝了 s2 重的鋼材時，兩車廂的最大裝載重量
    f = [[0] * (B + 1) for _ in range(A + 1)]
    for x in X:
        for j in range(A, -1, -1):
            for k in range(B, -1, -1):
                if j - x >= 0:
                    f[j][k] = max(f[j][k], f[j - x][k] + x)
                if k - x >= 0:
                    f[j][k] = max(f[j][k], f[j][k - x] + x)
    print(max(map(max, f)))

if __name__ == "__main__":
    solve()