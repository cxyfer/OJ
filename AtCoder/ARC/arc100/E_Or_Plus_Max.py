"""
ARC100C - Or Plus Max
https://atcoder.jp/contests/arc100/tasks/arc100_c
SOS DP

題意為對於每個 (i | j) <= k ，求 ai + aj 的最大值。
由於 <= k 這個條件很難處理，又每個 k 都需求一次答案，因此這個條件可以轉換 (i | j) == k，並求前綴最大值即可。

但 == k 還是很難處理，再調整一下，改成 (i | j) | k == k，即 i 和 j 是 k 的子集。
而求 ai + aj 的最大值，可以透過維護滿足條件的最大值和次大值來求解。
自此問題轉換成一個子集最大值的問題。
"""
def solve():
    n = int(input())
    A = list(map(int, input().split()))

    B = n
    U = 1 << B

    f = [[0, 0] for _ in range(U)]
    def update(s, x):
        if x > f[s][0]:
            f[s][0], f[s][1] = x, f[s][0]
        elif x > f[s][1]:
            f[s][1] = x

    for i, x in enumerate(A):
        update(i, x)

    for i in range(B):
        s = 0
        while s < U:
            s |= (1 << i)
            update(s, f[s ^ (1 << i)][0])
            update(s, f[s ^ (1 << i)][1])
            s += 1

    ans = []
    pre = 0
    for k in range(1, U):
        pre = max(pre, sum(f[k]))
        ans.append(pre)
    print(*ans, sep = "\n")

if __name__ == '__main__':
    solve()