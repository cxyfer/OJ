"""
P14360 [CSP-J 2025] 多边形 / polygon
https://www.luogu.com.cn/problem/P14360

由於是順序無關，所以可以先排序，從小到大枚舉集合的最大值 a[i]。
此時 a[i] 一定在集合中，因此 s + a[i] > 2 * a[i] 等價於 s > a[i]，其中 s 為其他所選數的和。
故對於 a[i] 來說，所求為在 a[1] ~ a[i-1] 中，選出至少兩個數，使得其和 > a[i] 的方案數。
但顯然只選 0 個數或 1 個數的情況不合法，因此只需考慮和 > a[i] 的方案數即可。

將不等式作為條件較難處理，因此可以轉換為等於的情況，這樣便可以用背包 DP 來實現，
令 f[i][j] 表示考慮前 i 個數，使得其和恰好 = j 的方案數。

但又有一個問題，考慮 > 時狀態數量過多，因此需要優化。
正難則反，改成計算所有方案減去不合法的情況即可，
在前 i - 1 個數中選若干的數的方案數為 2 ^ (i - 1)，不合法的方案數出現在 j <= x 的情況。
"""
MOD = 998244353

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    assert len(A) == n

    mx = A[-1]
    f = [1] + [0] * mx
    ans = 0
    for i, x in enumerate(A, start=1):
        if i >= 3:
            ans += (1 << (i - 1))
            ans %= MOD
            for j in range(x + 1):
                ans -= f[j]
                ans %= MOD
        for j in range(mx, x - 1, -1):
            f[j] += f[j - x]
            f[j] %= MOD
    print(ans)

if __name__ == "__main__":
    solve()