t = int(input())

for _ in range(t):
    a, b, c, d = map(int, input().split())

    if b - a > d - c:
        ans = [(a, d - 1), (b - 1, d), (b, d)]
    else:
        ans = [(b - 1, c), (b, d - 1), (b, d)]

    for (x, y) in ans:
        print(x, y)