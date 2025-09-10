"""
P2340 [USACO03FALL] Cow Exhibition G
https://www.luogu.com.cn/problem/P2340
背包DP：將其中一維視為 weight，另一維視為 value
因為負數很麻煩，所以直接用 defaultdict 來處理，對負數應用偏移的寫法見 C++ 版本
"""
from collections import defaultdict

def solve():
    N = int(input())
    cows = [list(map(int, input().split())) for _ in range(N)]

    # f[s] 表示智商和為 s 時，能達到的最大情商和
    f = defaultdict(lambda: float('-inf'))
    f[0] = 0
    for s_i, f_i in cows:
        nf = f.copy()
        for s_tot, f_tot in f.items():
            nf[s_tot + s_i] = max(nf[s_tot + s_i], f_tot + f_i)
        f = nf

    ans = 0
    for s_tot, f_tot in f.items():
        if s_tot >= 0 and f_tot >= 0:  # 題目限制
            ans = max(ans, s_tot + f_tot)
    print(ans)

if __name__ == "__main__":
    solve()