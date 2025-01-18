N, M = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i, x in enumerate(A):
    if x <= M:
        M -= x
        ans += 1
    else:
        break
print(ans)