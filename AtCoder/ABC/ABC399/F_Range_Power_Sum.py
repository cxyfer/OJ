"""
將第二個 Summation 寫成前綴和後，用二項式展開
"""
MOD = 998244353
N, K = map(int, input().split())
A = list(map(int, input().split()))

s = [0] * (N + 1)
for i in range(1, N + 1):
    s[i] = (s[i - 1] + A[i - 1]) % MOD


# 預先計算二項式係數 binom(K, p) (p = 0,...,K)
combk = [1] * (K + 1)
# 使用遞推公式:
# binom(K, p) = binom(K, p-1)*(K-p+1)/p
for p in range(1, K+1):
    combk[p] = combk[p-1] * (K - p + 1) // p
    combk[p] %= MOD

# S[t] = 累計之前所有前綴和之 t 次冪
# 因為 P[0] = 0，但約定 0^0 = 1，因此 S[0]=1，其餘 S[t] (t>=1) 為0
S = [0]*(K+1)
S[0] = 1  # P[0]^0

ans = 0
prefix = 0
for i in range(N):
    prefix = (prefix + A[i]) % MOD
    # 計算 powers[t] = (P[i])^t MOD MOD, t = 0,...,K
    powers = [1]*(K+1)
    for t in range(1, K+1):
        powers[t] = (powers[t-1] * prefix) % MOD
    
    # 對固定的 i，我們要加上 sum_{p=0}^K binom(K, p)*(-1)^{K-p}*(prefix)^p*S[K-p]
    cur = 0
    for p in range(K+1):
        # (-1)^(K-p) MOD MOD (我們用 MOD-1 代表 -1)
        sign = 1 if ((K-p) % 2 == 0) else (MOD - 1)
        term = combk[p] * sign % MOD
        term = term * powers[p] % MOD
        term = term * S[K-p] % MOD
        cur = (cur + term) % MOD
    ans = (ans + cur) % MOD
    
    # 更新 S[t]，加上目前的 (prefix)^t
    for t in range(K+1):
        S[t] = (S[t] + powers[t]) % MOD

print(ans)
