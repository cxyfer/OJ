from collections import deque

n, k = map(int, input().split())
A = list(map(int, input().split()))

if sum(A) < k:
    exit(print(-1))

# 二分搜尋找到最大完整輪數
def check(m):
    s = sum(min(m, a) for a in A)
    return s <= k

left, right = 0, 10**18
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        left = mid + 1
    else:
        right = mid - 1

# 模擬經過完整 right 輪後的結果
q = deque()
for i in range(n):
    t = min(right, A[i])
    A[i] -= t
    if A[i] > 0:
        q.append(i)
    k -= t

# 直接模擬最後一輪
while k > 0 and q:
    i = q.popleft()
    k -= 1
    A[i] -= 1
    if A[i] > 0:
        q.append(i)

print(*map(lambda x: x + 1, q))