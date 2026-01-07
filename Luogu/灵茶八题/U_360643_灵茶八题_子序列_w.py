"""
U360643 灵茶八题 - 子序列 +w^
https://www.luogu.com.cn/problem/U360643

01 背包
子序列的和可以看作是01背包問題，令 f[i][j] 表示從前 i 個數中選出元素和為 j 的方案數，
由於 j^j = 0，所以我們只需要知道 f[i][j] 的奇偶性即可。
- 初始值 f[0][0] = 1，其餘為 0。
- 狀態轉移方程為 f[i][j] = f[i - 1][j] ^ f[i - 1][j - a[i]]。
- 答案為 f[n][j] = 1 的 j 的異或和。

可以用位運算優化，令 f 為一個二進位數，第 j 位為 1 表示 f[j] 為奇數，為 0 表示 f[j] 為偶數。
轉移公式為 f ^= (f << a[i])，其中 a[i] 是第 i 個數。
最後答案為 f 中為 1 的位數的異或和。
"""
def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    f = 1
    for x in A:
        f ^= (f << x)
    
    ans = 0
    # for j in range(f.bit_length()):
    #     if f >> j & 1:
    #         ans ^= j
    while f:
        lb = f & -f
        ans ^= lb.bit_length() - 1
        f ^= lb
    print(ans)

if __name__ == "__main__":
    solve()