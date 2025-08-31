"""
CSES-1654 SOS Bit Problem
https://cses.fi/problemset/task/1654
SOS DP

1. 滿足 (x | y) == x 的 y 個數：x 的子集中的元素數量
2. 滿足 (x & y) == x 的 y 個數：x 的超集中的元素數量
3. 滿足 (x & y) != 0 的 y 個數：
  - 正難則反，所求為全部元素數量 n 減去 (x & y) == 0 的 y 個數
  - 而滿足 (x & y) == 0 的 y 個數，等價於 (~x | y) == (~x) 的 y 個數，故由 1. 可得
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
        # 這裡是從大的子集往小的子集更新，反過來做似乎也是對的
        for s in range(U - 1, -1, -1):
            if (s >> i) & 1:
                f2[s ^ (1 << i)] += f2[s]

    for x in A:
        print(f1[x], f2[x], n - f1[x ^ ((1 << BITS) - 1)])

if __name__ == '__main__':
    solve()