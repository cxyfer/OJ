n, k = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
m = n // 2

def check(mid):
    cnt = 0
    for i in range(m, n):
        if A[i] < mid:
            cnt += mid - A[i]
            if cnt > k:
                return False
    return cnt <= k

left, right = A[m], A[m] + k
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        left = mid + 1
    else:
        right = mid - 1
print(right)