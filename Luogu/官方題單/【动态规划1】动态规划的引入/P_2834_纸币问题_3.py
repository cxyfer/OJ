"""
P2834 纸币问题_3
https://www.luogu.com.cn/problem/P2834
背包DP模板題：求「組合」方案數
"""

MOD = int(1e9) + 7


def solve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == n

    # f[i][j] 表示考慮前i種紙幣，湊成j元的方案數
    f = [1] + [0] * k
    for x in A:
        # nf = f.copy()
        # for i in range(x, k + 1):
        #     nf[i] = (nf[i] + nf[i - x]) % MOD
        # f = nf
        for i in range(x, k + 1):
            f[i] = (f[i] + f[i - x]) % MOD
    print(f[k])


if __name__ == "__main__":
    solve()
