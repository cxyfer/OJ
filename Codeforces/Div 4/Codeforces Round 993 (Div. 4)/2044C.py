t = int(input())

for _ in range(t):
    m, a, b, c = map(int, input().split())
    ans = min(m, a) + min(m, b)
    ans += min(2 * m - ans, c)
    print(ans)
