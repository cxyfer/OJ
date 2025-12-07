"""
CSES-1746 Array Description
https://cses.fi/problemset/task/1746
"""
MOD = int(1e9 + 7)

def solve():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == n

    f = [0] * (m + 2)
    for i, x in enumerate(A):
        nf = [0] * (m + 2)
        x = A[i]
        if x == 0:
            for y in range(1, m + 1):
                nf[y] = (f[y - 1] + f[y] + f[y + 1] + (i == 0)) % MOD
        else:
            nf[x] = (f[x - 1] + f[x] + f[x + 1] + (i == 0)) % MOD
        f = nf
    print(sum(f) % MOD)

if __name__ == '__main__':
    solve()