n, k = map(int, input().split())

A = [int(input()) for _ in range(n)]

def check(x):
    return sum(a // x for a in A) >= k

left, right = 1, max(A)
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        left = mid + 1
    else:
        right = mid - 1
print(right)