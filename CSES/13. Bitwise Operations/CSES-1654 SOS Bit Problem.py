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
        # for s in range(U):
        #     if (s >> i) & 1:
        #         f1[s] += f1[s ^ (1 << i)]
        s = 0
        while s < U:
            s |= (1 << i)  # 優化：保證 (s >> i) & 1 成立
            f1[s] += f1[s ^ (1 << i)]
            s += 1

    for i in range(BITS):
        # for s in range(U - 1, -1, -1):
        #     if (s >> i) & 1:
        #         f2[s ^ (1 << i)] += f2[s]
        s = 0
        while s < U:
            s |= (1 << i)
            if s < U:
                f2[s ^ (1 << i)] += f2[s]
            s += 1

    for x in A:
        print(f1[x], f2[x], n - f1[x ^ ((1 << BITS) - 1)])

if __name__ == '__main__':
    solve()

