T = int(input())

for tc in range(1, T+1):
    digits = list(map(int, list(input())))
    cur = 1
    ans = 0
    for d in digits:
        d = 10 if d == 0 else d
        if cur != d:
            ans += abs(cur - d)
            cur = d
        ans += 1
    print(ans)