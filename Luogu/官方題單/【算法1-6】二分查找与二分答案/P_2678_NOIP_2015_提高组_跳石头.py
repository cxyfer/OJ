L, N, M = map(int, input().split())

A = [int(input()) for _ in range(N)]

def check(x):
    cnt = last = 0
    for a in A:
        if a - last < x:
            cnt += 1
        else:
            last = a
    if L - last < x:
        cnt += 1
    return cnt <= M

left, right = 1, L
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        left = mid + 1
    else:
        right = mid - 1
print(right)