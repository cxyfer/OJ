t = int(input())

for _ in range(t):
    n = int(input())
    P = list(map(int, input().split()))
    pos = [0] * (n + 1)
    for m, x in enumerate(P):
        pos[x] = m
    ans = ['0'] * n
    mn = mx = pos[1]
    for m in range(1, n + 1):
        mn = min(mn, pos[m])
        mx = max(mx, pos[m])
        if (mx - mn + 1) == m:
            ans[m - 1] = '1'
    print(''.join(ans))