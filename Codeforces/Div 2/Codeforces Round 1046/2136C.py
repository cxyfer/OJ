"""
2136C - Against the Difference 
https://codeforces.com/contest/2136/problem/C
DP
"""
def solve():
    n = int(input())
    A = list(map(int, input().split()))

    f = [0] * (n + 1)
    pos = [[] for _ in range(n + 1)]

    for i, x in enumerate(A, start=1):
        pos[x].append(i)
        m = len(pos[x])
        if m >= x:
            f[i] = max(f[i - 1], f[pos[x][m - x] - 1] + x)
        else:
            f[i] = f[i - 1]
    print(f[n])

t = int(input())
for _ in range(t):
    solve()