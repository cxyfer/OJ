n = int(input())

for _ in range(n):
    e, f, c = map(int, input().split())
    ans = 0
    cur = e + f
    while cur >= c:
        q, r = divmod(cur, c)
        ans += q
        cur = q + r
    print(ans)