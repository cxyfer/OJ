from atcoder.fenwicktree import FenwickTree

MOD = 998244353

def solve():
    n = int(input())
    P = list(map(int, input().split()))
    assert len(P) == n

    L = [0] * n
    bit1 = FenwickTree(n + 1)
    for i, x in enumerate(P):
        L[i] = bit1.sum(0, x)
        bit1.add(x, 1)

    R = [0] * n
    bit2 = FenwickTree(n + 1)
    for i in range(n - 1, -1, -1):
        x = P[i]
        R[i] = bit2.sum(0, x)
        bit2.add(x, 1)

    pow2 = [1] * (n + 1)
    for i in range(1, n + 1):
        pow2[i] = pow2[i - 1] * 2 % MOD
    inv2 = [-1] * (n + 1)
    inv2[n] = pow(pow2[n], -1, MOD)
    for i in range(n - 1, -1, -1):
        inv2[i] = inv2[i + 1] * 2 % MOD

    ans = 0
    for a, b in zip(L, R):
        ans += a * b
        ans %= MOD

    # for i in range(n):
    #     for j in range(i + 1, n):
    #         ans += L[i] * R[j] * pow2[j - i - 1]
    #         ans %= MOD
    s = 0
    for j in range(n):
        if j > 0:
            ans += s * R[j] * pow2[j - 1]
            ans %= MOD
        s += L[j] * inv2[j]
        s %= MOD
    print(ans)

if __name__ == '__main__':
    solve()