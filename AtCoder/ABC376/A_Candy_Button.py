N, C = map(int, input().split())
T = list(map(int, input().split()))

T.sort()

ans = 0
last = -float("inf")
for t in T:
    if t >= last + C:
        ans += 1
        last = t
print(ans)