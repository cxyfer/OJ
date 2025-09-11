"""
D. 小苯的子序列权值
https://ac.nowcoder.com/acm/contest/116658/D

一個數是否是偶數是由二進位下的最低位是否為 0 決定，而只要有至少一個偶數，那麼 AND 的結果就一定是偶數。
正難則反，計算全部的非空子序列數量減去不包含偶數的非空子序列數量即可。
"""
MOD = 998244353

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n
    cnt = [0, 0]
    for x in A:
        cnt[x & 1] += 1
    print(((pow(2, n, MOD) - 1) - (pow(2, cnt[1], MOD) - 1)) % MOD)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()