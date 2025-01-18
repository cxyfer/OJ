T = int(input())

for tc in range(1, T+1):
    MOD = 998244353
    N = int(input())
    p = list(map(int, input().split()))
    n = len(p)
    p = [(p[i], i) for i in range(n)]
    p.sort()

    dp = [0]*(n+1)
    dp[0] = 1
    prefix = [1]*(n+1)
    l = r = -1

    for i in range(n):
        _, idx = p[i]
        l = min(l, idx) if l != -1 else idx
        r = max(r, idx) if r != -1 else idx
        dp[i+1] = (prefix[r] - (prefix[l-1] if l > 0 else 0)) % MOD
        prefix[i+1] = (prefix[i] + dp[i+1]) % MOD

    print(dp[n])

