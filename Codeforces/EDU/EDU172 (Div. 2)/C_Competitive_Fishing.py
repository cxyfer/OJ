t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    s = s[::-1]

    ps = [0] * (n + 1)
    for i in range(n):
        ps[i + 1] = ps[i] + (1 if s[i] == '1' else -1)

    A = sorted(ps[1:-1], reverse=True)
    tot = 0
    for i in range(1, n):
        tot += A[i - 1]
        if tot >= k:
            print(i + 1)
            break
    else:
        print(-1)