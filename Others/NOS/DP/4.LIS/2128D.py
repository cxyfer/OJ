"""
CF2128D Sum of LDS
https://codeforces.com/problemset/problem/2128/D

所求為 sum(LDS(P[l...r])) 的值。
由於題目保證 max(P[i], P[i + 1]) > P[i + 2]，因此 i 的後綴最大值只可能為 P[i] 或 P[i + 1]。
令 f[i] 表示固定 i 為左端點時，所有區間的 LDS 的長度之和，
即 f[i] = sum(LDS(P[i...r]) for r in range(i, n))，則所求為變為 sum(f[i])。

考慮兩種情況：
1. P[i] > P[i + 1]，則此時左端點為 i + 1 的區間，都能透過在左側加上 P[i] 來增加 LDS 的長度，
   這樣的區間有 n - (i + 1) 個，再加上 [i, i] 這個區間，因此 f[i] = f[i + 1] + (n - i)
2. P[i] < P[i + 1]，則上述的 n - (i + 1) 個區間，都不能透過在左側加上 P[i] 來增加 LDS 的長度，
   只有 [i, i] 這個區間本身對 f[i] 有貢獻，因此 f[i] = f[i + 1] + 1
"""


def solve():
    n = int(input())
    P = list(map(int, input().split()))

    f = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        if i + 1 < n and P[i] > P[i + 1]:
            f[i] = f[i + 1] + (n - i)
        else:
            f[i] = f[i + 1] + 1
    print(sum(f))


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
