"""
正解是透過完全背包的生成函數，透過多項式卷積，使用 Bostan-Mori 求解。

補題的時候找到一篇有趣的題解，主要思路如下：
1. 利用二進位拆分，逐位求解
2. 進位時壓縮背包
https://www.luogu.com.cn/article/6s0p6rfr
"""
MOD = 998244353

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == N

    # S + 1/2S + 1/4S + ... = 2S
    # 狀態空間上限大約是 sum(A) 的兩倍
    MAX_W = sum(A) * 2
    
    f = [0] * (MAX_W + 1)
    f[0] = 1

    # 逐位處理
    while M > 0:
        # 1. 0/1 背包階段：決定當前位每個 x_i 是否為 1
        for x in A:
            for j in range(MAX_W, x - 1, -1):
                f[j] = (f[j] + f[j - x]) % MOD

        # 2. 壓縮階段：計算進位並壓縮狀態
        nf = [0] * (MAX_W + 1)
        d = M & 1
        for j in range(MAX_W + 1):
            # 根據不等式 j <= d + 2 * nj 推導出 nj = ceil((j - d) / 2)
            nj = (j - d + 1) >> 1
            nf[nj] = (nf[nj] + f[j]) % MOD

        f = nf
        M >>= 1
    print(f[0])

if __name__ == '__main__':
    solve()