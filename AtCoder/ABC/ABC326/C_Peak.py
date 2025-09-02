N, M = map(int, input().split())
As = list(map(int, input().split()))

As.sort()
As = As
ans = tmp = 0
l = 0
for idx, num in enumerate(As):
    tmp += 1
    while num - As[l] >= M:
        tmp -= 1
        l += 1
    ans = max(ans, tmp)
ans = max(ans, tmp)
print(ans)