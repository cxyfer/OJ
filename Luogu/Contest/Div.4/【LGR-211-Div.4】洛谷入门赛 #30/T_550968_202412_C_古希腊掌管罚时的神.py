n = int(input())

ans = 0
for _ in range(n):
    a, b = map(int, input().split())
    ans += 20 if b == 0 else a
print(ans)