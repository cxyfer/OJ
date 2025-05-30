from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))

ans = left = 0
cnt = defaultdict(int)
for right, x in enumerate(A):
    cnt[x] += 1
    while cnt[x] > 1:
        cnt[A[left]] -= 1
        left += 1
    ans += right - left + 1
print(ans)