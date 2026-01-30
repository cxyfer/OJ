from functools import cache
from collections import defaultdict

MOD = int(1e9 + 7)

def solve():
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    """1. 使用 @cache 裝飾器實現記憶化搜索，但會有遞歸深度限制以及雜湊效率較低的問題"""
    # @cache
    # def dfs(msk: int) -> int:
    #     i = msk.bit_count()
    #     if i == N:
    #         return 1
    #     res = 0
    #     for j in range(N):
    #         if msk & (1 << j) or grid[i][j] == 0:
    #             continue
    #         res = (res + dfs(msk | (1 << j))) % MOD
    #     return res
    # print(dfs(0))

    """2. 將 DFS 轉換成 Stack 實現記憶化搜索"""
    U = 1 << N
    f = [-1] * U
    st = [(0, 0)]  # (msk, flag)
    while st:
        msk, flag = st.pop()
        i = msk.bit_count()
        if f[msk] != -1:
            continue
        if i == N:
            f[msk] = 1
            continue
        if flag == 0:
            st.append((msk, 1))
            for j in range(N):
                if msk & (1 << j) or grid[i][j] == 0:
                    continue
                st.append((msk | (1 << j), 0))
        else:
            res = 0
            for j in range(N):
                if msk & (1 << j) or grid[i][j] == 0:
                    continue
                res = (res + f[msk | (1 << j)]) % MOD
            f[msk] = res
            continue
    print(f[0])

    """3. 用遞推的方式實現"""
    # U = 1 << N
    # f = defaultdict(int)
    # f[0] = 1
    # for i in range(N):
    #     nf = defaultdict(int)
    #     for msk, val in f.items():
    #         for j in range(N):
    #             if msk & (1 << j) or grid[i][j] == 0:
    #                 continue
    #             nf[msk | (1 << j)] += val
    #             nf[msk | (1 << j)] %= MOD
    #     f = nf
    # print(f[U - 1])

if __name__ == "__main__":
    solve()