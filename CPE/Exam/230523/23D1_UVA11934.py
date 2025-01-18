while True:
    a, b, c, d, L = map(int, input().split())
    if all(x == 0 for x in [a, b, c, d, L]):
        break
    ans = 0
    for x in range(L+1): # [0, L]
        if (a * x * x + b * x + c) % d == 0:
            ans += 1
    print(ans)