"""
CSES-1654 SOS Bit Problem
https://cses.fi/problemset/task/1654

SOS DP
"""
def solve():
    n = int(input())
    A = list(map(int, input().split()))

    BITS = max(A).bit_length()
    U = 1 << BITS

    f1 = [0] * U  # 子集(subset)
    f2 = [0] * U  # 超集(supermask)
    for x in A:
        f1[x] += 1
        f2[x] += 1

    for i in range(BITS):
        for msk in range(U):
            if (msk >> i) & 1:
                f1[msk] += f1[msk ^ (1 << i)]

    for i in range(BITS):
        for msk in range(U - 1, -1, -1):
            if (msk >> i) & 1:
                f2[msk ^ (1 << i)] += f2[msk]

    for x in A:
        print(f1[x], f2[x], n - f1[x ^ ((1 << BITS) - 1)])

if __name__ == '__main__':
    solve()

