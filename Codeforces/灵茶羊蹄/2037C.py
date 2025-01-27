t = int(input())

for _ in range(t):
    n = int(input())

    if n < 5:
        print(-1)
        continue

    odds, evens = [], []
    for x in range(1, n + 1):
        if x == 4 or x == 5:
            continue
        if x & 1:
            odds.append(x)
        else:
            evens.append(x)

    ans = odds + [5, 4] + evens
    print(*ans)