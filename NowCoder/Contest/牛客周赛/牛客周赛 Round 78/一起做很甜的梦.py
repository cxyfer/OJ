n = int(input())

ans = [-1] * n
l, r = 0, n - 1
for i in range(1, n + 1):
    if i & 1:
        ans[l] = i
        l += 1
    else:
        ans[r] = i
        r -= 1
print(*ans)