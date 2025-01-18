t = int(input())

for _ in range(t):
    n = int(input())
    ans = cur = 1
    while cur < n:
        cur = (cur + 1) * 2
        ans += 1
    print(ans)