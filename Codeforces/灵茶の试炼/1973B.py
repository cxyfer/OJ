t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))

    pos = [[-1] for _ in range(20)]
    for i in range(n):
        for b in range(20):
            if (A[i] >> b) & 1:
                pos[b].append(i)
    for b in range(20):
        pos[b].append(n)
    ans = 0
    for b in range(20):
        if len(pos[b]) <= 2:
            continue
        for i in range(len(pos[b]) - 1):
            ans = max(ans, pos[b][i + 1] - pos[b][i])
    print(ans if ans > 0 else 1)