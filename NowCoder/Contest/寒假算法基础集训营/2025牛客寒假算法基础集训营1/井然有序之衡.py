n = int(input())
A = list(map(int, input().split()))

if sum(A) != n * (n + 1) // 2:
    exit(print(-1))

A.sort()
ans = 0
for i, x in enumerate(A):
    ans += abs(x - (i + 1))
print(ans // 2)