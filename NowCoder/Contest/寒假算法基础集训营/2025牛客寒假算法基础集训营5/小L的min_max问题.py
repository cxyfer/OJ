"""
H - 小L的min_max问题
https://ac.nowcoder.com/acm/contest/95337/H

考慮每一個區間 [l, r] 對答案的貢獻。
此時在 [0, l - 1] 以及 [r + 1, n - 1] 中還需要取 k - 1 個區間
令 x, y 分別表示 [0, l - 1] 和 [r + 1, n - 1] 中的大小，枚舉在左側選擇的區間數量 i，則右側還需選 k - 1 - i 個區間
利用隔板法，可以得到左側為在 x + 1 - 2 個位置中選擇 i - 1 個位置放置隔板，有 C(x - 1, i - 1) 種選擇方式；
同理，右側有 C(y - 1, k - i - 2) 種選擇方式。
總共有 sum(C(x - 1, i - 1) * C(y - 1, k - i - 2)) 種選擇方式，其中 0 <= i <= k - 1。

可以用一些數學推導來省略枚舉，但其實可以簡單地利用隔板法來思考。
將左右兩側合併，中間視為已經插入一個隔板，則此時需要再插入 k - 3 個隔板，才能將區間分成 k 個區間
也就是需要在 (x - 1) + (y - 1) 個位置中選擇 k - 3 個位置放置隔板，有 C(x + y - 2, k - 3) 種選擇方式。

注意上述討論的是 x > 0 && y > 0 && k >= 3 的情況，其他情況需要特判。
"""
MOD = 998244353

MAX_N = int(3e3 + 5)
fact = [1] * (MAX_N + 1)
for i in range(1, MAX_N + 1):
    fact[i] = fact[i - 1] * i % MOD
invf = [0] * (MAX_N + 1)
invf[MAX_N] = pow(fact[MAX_N], MOD - 2, MOD)
for i in range(MAX_N - 1, -1, -1):
    invf[i] = (invf[i + 1] * (i + 1)) % MOD

def comb(n, k):
    assert n >= k >= 0
    return fact[n] * invf[k] * invf[n - k] % MOD

def solve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 0
    for l in range(n):
        mn, mx = float('inf'), float('-inf')
        x = l
        for r in range(l, n):
            y = n - 1 - r
            if x + y < k - 1:
                break
            mn = min(mn, A[r])
            mx = max(mx, A[r])
            if l == 0 and r == n - 1 and k == 1:
                cnt = 1
            elif l == 0 and k >= 2:
                cnt = comb(y - 1, k - 2)
            elif r == n - 1 and k >= 2:
                cnt = comb(x - 1, k - 2)
            elif k >= 3:
                cnt = comb(x + y - 2, k - 3)
            else:
                cnt = 0
            ans += mx * mn * cnt % MOD
            ans %= MOD
    print(ans % MOD)

if __name__ == "__main__":
    solve()