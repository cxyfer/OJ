MAX_DAYS = 3660
T = int(input())

for _ in range(T):
    N = int(input()) # of days
    P = int(input()) # of parties
    H = [int(input()) for _ in range(P)]

    days = [0] * (N + 1)
    for h in H:
        for i in range(h, N + 1, h):
            days[i] = 1
    ans = 0
    for i in range(1, N + 1):
        if i % 7 == 6 or i % 7 == 0:
            continue
        ans += days[i]
    print(ans)