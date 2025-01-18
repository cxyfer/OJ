t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))

    ans = 0
    s = 0
    d = 1
    for i, x in enumerate(A):
        s += x
        while s > d * d:
            d += 2
        if s == d * d:
            ans += 1
    print(ans)