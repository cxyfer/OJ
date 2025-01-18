T = int(input())

for tc in range(1, T+1):
    n = int(input())
    ans = ""
    while n:
        q, r = divmod(n, -2)
        if r < 0:
            q += 1
            r += 2
        ans += str(r)
        n = q
    print(f"Case #{tc}: {ans[::-1] if ans else 0}")
