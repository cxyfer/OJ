t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    x = [0] * (n + 1)
    for i in range(1, n + 1):
        if A[i - 1] > x[i - 1]:
            x[i] = x[i-1] + 1
        elif A[i - 1] == x[i - 1]:
            x[i] = x[i - 1]
        else:
            x[i] = x[i - 1] - 1

    min_xr = [0] * (n + 1) + [float('inf')]
    for l in range(n, 0, -1):
        min_xr[l] = min(x[l], min_xr[l + 1])

    ans = -float('inf')
    for l in range(1, n + 1):
        ans = max(ans, x[l - 1] - min_xr[l])

    print(x[n] + ans if ans > 0 else x[n] - 1)
    