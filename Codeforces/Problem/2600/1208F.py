"""
CF1208F - Bits And Pieces
https://codeforces.com/contest/1208/problem/F
SOS DP

所求為滿足 i < j < k 的最大 ai | (aj & ak)。
由於 | 只會使數字變大，考慮枚舉 ai，貪心地從高位到低位構建 (aj & ak) 的值。

令 f[S] 為滿足 ai & S == S 的元素中，最大的兩個下標 k, j，
則若 f[S][1] > i，則可以得到滿足的一組下標 (i, j, k)。
"""
def solve():
    n = int(input())
    A = list(map(int, input().split()))
    B = max(A).bit_length()
    U = 1 << B

    f1 = [-1] * U
    f2 = [-1] * U
    def update(s, i):
        if i > f1[s]:
            f1[s], f2[s] = i, f1[s]
        elif i > f2[s]:
            f2[s] = i

    for i, x in enumerate(A):
        update(x, i)
    
    # SOS DP
    for i in range(B):
        # for s in range(U - 1, -1, -1):
        #     if (s >> i) & 1:
        #         update(s ^ (1 << i), f[s][0])
        #         update(s ^ (1 << i), f[s][1])
        s = 0
        while s < U:
            s |= (1 << i)
            update(s ^ (1 << i), f1[s])
            update(s ^ (1 << i), f2[s])
            s += 1

    ans = 0
    for i in range(n - 2):
        x = A[i]
        s = 0
        # 貪心從高位到低位構建 s = aj & ak
        for b in range(B - 1, -1, -1):
            if (x >> b) & 1:  # 這位可以由 ai 貢獻，不用考慮 aj & ak
                continue
            if f2[s | (1 << b)] > i:
                s |= (1 << b)
        ans = max(ans, x | s)
    print(ans)

if __name__ == '__main__':
    solve()