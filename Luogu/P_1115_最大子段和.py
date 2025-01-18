n = int(input())
A = list(map(int, input().split()))

ans = -float('inf')
cur = 0
for x in A:
    cur = max(cur + x, x)
    ans = max(ans, cur)
print(ans)