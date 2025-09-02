N = int(input())
A = list(map(int, input().split()))
mx = max(A)
ans = 0
for num in A:
    if num < mx:
        ans = max(ans, num)
print(ans)