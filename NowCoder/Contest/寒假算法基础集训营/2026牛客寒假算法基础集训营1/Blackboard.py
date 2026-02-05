"""
H. Blackboard
https://ac.nowcoder.com/acm/contest/120561/H
位運算 + 前綴和優化 DP

根據題意，可以將 A[i] 分成若干段，每一段中都只有 OR 運算，且不同段間使用 + 連結。
形如 (OR(A[0...p-1])) + (OR(A[p...q-1])) + ... + (OR(A[q...n-1])) = SUM(A[0...n-1])
對於每一段而言，由於 OR 的性質，OR(A[p...q-1]) <= SUM(A[p...q-1])，
因此要使等號成立，則每一段的 OR 值都必須取等號，也就是每一段的 SUM 值都必須為 OR 值，
而 OR 是不進位加法，因此等號成立於每一段「不發生進位」，即任兩個元素的 AND 值為 0。

定義 f[i] 表示考慮前 i 個元素，且第 i 個元素 (A[i-1]) 作為某段結尾時的方案數，
則 f[i] = sum(f[j] for j in range(i) if OR(A[j...i-1]) = SUM(A[j...i-1]))
然而轉移是 O(n) 的，因此需要優化。

注意到當 i 固定時，若 j 無法轉移到 i，則 j - 1 也無法轉移到 i，轉移來源是一個連續區間，
故可以利用前綴和優化轉移，並使用滑動窗口維護轉移來源的區間。
"""
MOD = 998244353

def solve():
    n = int(input())
    A = list(map(int, input().split()))

    f = [1] + [0] * n
    s = [0] * (n + 2)
    for i in range(1, n + 2):
        s[i] = s[i - 1] + f[i - 1]

    cnt = [0] * 32
    left = or_val = 0
    for r, x in enumerate(A, start=1):
        # 出窗口
        while (or_val & x) != 0:  # 加入 x 後會發生進位
            # 移除左側的元素，直到不會發生進位為止
            y = A[left]
            for b in range(32):
                if (y >> b) & 1:
                    cnt[b] -= 1
                    if cnt[b] == 0:
                        or_val &= ~(1 << b)
            left += 1

        # 入窗口
        for b in range(32):
            if (x >> b) & 1:
                cnt[b] += 1
        or_val |= x

        # 更新答案
        f[r] = (s[r] - s[left]) % MOD  # 轉移區間來自 [left, r)
        s[r + 1] = (s[r] + f[r]) % MOD

    print(f[n])

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()