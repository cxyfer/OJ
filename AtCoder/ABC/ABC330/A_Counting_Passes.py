N, L = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for s in A:
    if s >= L:
        ans += 1

print(ans)