"""
腦筋急轉彎

由於是把所有 pair 相乘後，對 2^64 取模，因此可以計算有多少 pair 可以貢獻多少 2^1，

考慮最低位，若 x ^ y 的最低位為 0，則可以貢獻至少一個 2^1，
而 x ^ y 的最低位為 0 的條件是 x 和 y 的最低位相同，也就是都是偶數或都是奇數。

統計偶數和奇數的數量，計算貢獻 2^1 的 pair 數量即可。
如果貢獻 2^1 的 pair 數量超過 64 個，則答案必定為 0。
"""

T = int(input())
MOD = 1 << 64

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    cnt = [0, 0]
    for x in A:
        cnt[x & 1] += 1

    if cnt[0] * (cnt[0] - 1) // 2 + cnt[1] * (cnt[1] - 1) // 2 >= 64:
        print(0)
    else:
        ans = 1
        for i, x in enumerate(A):
            for j in range(i + 1, N):
                ans = ans * (A[i] ^ A[j]) % MOD
        print(ans)