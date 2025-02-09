n = 5
A = list(map(int, input().split()))

ans = 0
for i, x in enumerate(A):
    ans += x % 3
    A[i] = x // 3
    A[(i - 1) % n] += x // 3
    A[(i + 1) % n] += x // 3

print(*A)
print(ans)