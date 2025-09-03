"""
pF_UVA-10690 Expression Again
https://vjudge.net/problem/UVA-13242
Prefix Sum

Python TLE, C++ AC
"""
def solve():
    V, T = map(int, input().split())
    N = int(input())
    jars = [list(map(int, input().split())) for _ in range(N)]

    sv = [0] * (N + 1)
    sw = [0] * (N + 1)
    for i in range(N):
        sv[i + 1] = sv[i] + jars[i][0]
        sw[i + 1] = sw[i] + jars[i][0] * jars[i][1]

    ans = (-1, -1)
    mnd = float('inf')
    for i in range(N):
        for j in range(i, N):
            v = sv[j + 1] - sv[i]
            w = sw[j + 1] - sw[i]
            # V / 2 <= v <= V 且 T - 5 <= w / v <= T + 5
            if (V <= 2 * v and v <= V) and (T - 5) * v <= w <= (T + 5) * v:
                d = abs(w / v - T)
                if d < mnd:
                    mnd = d
                    ans = (i, j)
                # elif d == mnd:
                #     if j - i < ans[1] - ans[0]:
                #         ans = (i, j)

    if ans == (-1, -1):
        print("Not possible")
    else:
        print(ans[0], ans[1])

t = int(input())
for _ in range(t):
    solve()