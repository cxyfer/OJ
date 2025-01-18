t = int(input())

for _ in range(t):
    n = int(input())
    P = list(range(n, 0, -1))
    print(*P)

    # A = [-1] * n
    # for i in range(n):
    #     A[i] = P[i] + P[P[i] - 1]
    # print(*A)