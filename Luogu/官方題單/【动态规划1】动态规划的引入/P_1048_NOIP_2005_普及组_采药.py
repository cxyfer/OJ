"""
P1048 [NOIP 2005 普及组] 采药
https://www.luogu.com.cn/problem/P1048
背包DP模板題：01背包求極值
"""


def solve():
    T, M = map(int, input().split())
    items = [list(map(int, input().split())) for _ in range(M)]

    # f[i][j] 表示考慮前i個物品，容量為j時的最大價值
    f = [0] * (T + 1)
    for t, v in items:
        nf = f.copy()
        for j in range(t, T + 1):
            nf[j] = max(nf[j], f[j - t] + v)
        f = nf
        # for j in range(T, t - 1, -1):  # 注意這裡的方向
        #     f[j] = max(f[j], f[j - t] + v)
    print(f[T])


if __name__ == "__main__":
    solve()
