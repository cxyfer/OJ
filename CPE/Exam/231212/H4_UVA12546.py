MOD = 10**9 + 7
T = int(input())

for tc in range(1, T+1):
    C = int(input())
    PA = [list(map(int, input().split())) for _ in range(C)]
    
    ans, n = 1, 1
    for (p, a) in PA:
        sigma, cur = 1, 1
        for _ in range(1, a+1): # p^1 + p^2 + ... + p^a
            cur = (cur * p) % MOD
            sigma = (sigma + cur) % MOD
        ans *= (sigma + a * cur) % MOD
        n *= cur
    ans = (ans + n) % MOD
    print("Case %d: %d" % (tc, ans))