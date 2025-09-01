"""
CSES-1654 SOS Bit Problem
https://cses.fi/problemset/task/1654
Sum over Subsets (SOS) DP 模板題

1. 滿足 (x | y) == x 的 y 個數：x 的子集(subset)中的元素數量
2. 滿足 (x & y) == x 的 y 個數：x 的超集(superset)中的元素數量
3. 滿足 (x & y) != 0 的 y 個數：
  - 正難則反，所求為全部元素數量 n 減去 (x & y) == 0 的 y 個數
  - 而滿足 (x & y) == 0 的 y 個數，等價於 (~x | y) == (~x) 的 y 個數，故由 1. 可得

轉移順序說明：
以子集和為例，當枚舉到第 i 位（或第 i 維）時，一定是從該位為 0 的位置轉移而來，
因此在計算第 i 位時，轉移來源一定不會被修改過，
故可以從小到大或從大到小皆可，計算超集和時同理。
"""
def solve():
    n = int(input())
    A = list(map(int, input().split()))

    B = max(A).bit_length()
    U = 1 << B

    f1 = [0] * U  # 子集(subset)
    f2 = [0] * U  # 超集(superset)
    for x in A:
        f1[x] += 1
        f2[x] += 1

    for i in range(B):
        # for s in range(U):
        #     if (s >> i) & 1:
        #         f1[s] += f1[s ^ (1 << i)]
        s = 0
        while s < U:
            s |= (1 << i)  # 優化：快速跳到 (s >> i) & 1 成立的位置
            f1[s] += f1[s ^ (1 << i)]
            s += 1

    for i in range(B):
        # 直覺上要從大的子集往小的子集更新，但其實反過來做也對，因此套用同樣的優化
        s = 0
        while s < U:
            s |= (1 << i)  # 優化：快速跳到 (s >> i) & 1 成立的位置
            f2[s ^ (1 << i)] += f2[s]
            s += 1

    for x in A:
        print(f1[x], f2[x], n - f1[x ^ ((1 << B) - 1)])

if __name__ == '__main__':
    solve()