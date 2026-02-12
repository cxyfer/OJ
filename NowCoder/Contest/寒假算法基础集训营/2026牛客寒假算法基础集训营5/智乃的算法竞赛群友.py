"""
F. 智乃的算法竞赛群友
https://ac.nowcoder.com/acm/contest/120565/F

貪心做法：

首先考慮是否有公共的前後綴，顯然只有 qcjjkkt 的後綴和 td 的前綴 t 是公共的。
而又 qcjjkktd 可以比 qcjjkkt/td 節省 1 個字元，因此優先使用 qcjjkktd 而不是 qcjjkkt/td。

那麼可以考慮 qcjjkkt 的數量 k，則剩餘 r = n - k * 7 個字元，
此時應該優先使用公共的部分，因此有 min(k, r) 個 qcjjkktd，剩餘只能取 td 了。

f(k) = k * a + min(k, n - 7k) * b + ((n - 7k) - min(k, (n - 7k))) // 2 * b
這是一個分段函數，極值只會發生在端點 0, n // 7，以及 n / 8 附近。

DP作法：

由於 lcm(2, 7, 8) = 56，因此每 56 個字元可以看作一個循環，
對於 [56k, 56k + 55] 這個區間，可以用 DP 來計算最大的價值。
"""
def solve():
    n, a, b = map(int, input().split())

    def calc(k):
        if k * 7 > n:
            return float('-inf')
        res = k * a  # qcjjkkt

        r = n - k * 7
        res += min(k, r) * b  # qcjjkktd
        r -= min(k, r)

        res += (r // 2) * b  # td
        return res
    
    ans = float('-inf')
    for k in [0, n // 8, n // 8 + 1, n // 7]:
        ans = max(ans, calc(k))
    print(ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()