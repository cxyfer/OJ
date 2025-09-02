N, M = map(int, input().split())
MOD = 998244353

g = [[0] * N for _ in range(N)]
for _ in range(M):
    u, v = map(lambda x: int(x) - 1, input().split())
    g[u][v] += 1
    g[v][u] += 1

ans1 = 0
for u in range(N):
    for v in range(u + 1, N):
        ans1 += g[u][v] * (g[u][v] - 1) // 2
        ans1 %= MOD

f = [[0] * N for _ in range(1 << N)]
for s in range(N):
    f[1 << s][s] = 1

ans2 = 0
for msk in range(1, 1 << N):
    s = (msk & -msk).bit_length() - 1
    t1 = msk ^ (1 << s)
    while t1:
        lb1 = t1 & -t1
        u = lb1.bit_length() - 1
        t1 ^= lb1
        t2 = prev = msk ^ lb1
        while t2:
            lb2 = t2 & -t2
            v = lb2.bit_length() - 1
            t2 ^= lb2
            f[msk][u] += f[prev][v] * g[v][u]
            f[msk][u] %= MOD
    if msk.bit_count() < 3:
        continue
    t = msk ^ (1 << s)
    while t:
        lb = t & -t
        u = lb.bit_length() - 1
        t ^= lb
        ans2 += f[msk][u] * g[u][s]
        ans2 %= MOD

ans2 *= pow(2, MOD - 2, MOD)
ans2 %= MOD
print((ans1 + ans2) % MOD)