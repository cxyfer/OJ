a, b, c, d, x = map(int, [input() for _ in range(5)])

ans = 0
if x >= a:
    ans += b
if x >= c:
    ans += d

print(ans)