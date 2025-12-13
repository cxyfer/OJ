"""
CF626F. Group Projects
https://codeforces.com/contest/626/problem/F

Open and Close Interval Trick
https://codeforces.com/blog/entry/47764

Same as CSES-1665 Coding Company
"""
MOD = int(1e9 + 7)

def solve():
    n, V = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == n

    A.sort()
    m = n >> 1  # 開啟的組數最多為 n/2

    f = [[0] * (V + 1) for _ in range(m + 1)]
    f[0][0] = 1
    for i, x in enumerate(A):
        nf = [[0] * (V + 1) for _ in range(m + 1)]
        d = x - (A[i - 1] if i > 0 else 0)
        for j in range(min(i + 1, m) + 1):
            cost = j * d
            for s in range(V - cost + 1):
                v = f[j][s] % MOD
                if not v: continue
                # 1. 開啟新組 (j -> j + 1)
                if j + 1 <= m: nf[j + 1][s + cost] += v
                # 2. 關閉舊組 (j -> j - 1)
                if j > 0: nf[j - 1][s + cost] += v * j
                # 3. 加入現有組或單獨一組 (j -> j)
                nf[j][s + cost] += v * (j + 1)
        f = nf
    print(sum(f[0]) % MOD)

if __name__ == '__main__':
    solve()