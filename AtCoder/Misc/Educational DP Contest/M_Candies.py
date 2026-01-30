from itertools import accumulate

MOD = int(1e9 + 7)

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == N

    f = [0] * (K + 1)
    f[0] = 1
    for x in A:
        nf = [0] * (K + 1)
        # for k in range(K + 1):
        #     for j in range(x + 1):
        #         if k - j >= 0:
        #             nf[k] = (nf[k] + f[k - j]) % MOD
        s = list(accumulate(f, lambda x, y: (x + y) % MOD, initial=0))
        for k in range(K + 1):
            nf[k] = (s[k + 1] - s[max(0, k - x)]) % MOD
        f = nf
    print(f[K])

if __name__ == "__main__":
    solve()