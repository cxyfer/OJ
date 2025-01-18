t = int(input())

for ts in range(t):
    N = int(input())
    P = list(map(int, input().split()))
    P.sort()

    X = P[:N]
    Y = P[N:]
    ans = 0
    for i in range(N-1):
        ans += (X[i+1] - X[i])
        ans += (Y[i+1] - Y[i])
    print(ans)
    for i in range(N):
        print(X[i], Y[i])