n = int(input())
A = list(map(int, input().split()))

B = [-1] * (n + 1)
for i, x in enumerate(A):
    B[x] = i

ans = 1
for x in range(2, n + 1):
    if B[x - 1] > B[x]:  # 需要額外一輪才能收集到 x
        ans += 1
print(ans)