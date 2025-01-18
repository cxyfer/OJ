L, N, K = map(int, input().split())

A = list(map(int, input().split()))

def check(x):
    cnt = 0
    for i in range(1, N):
        d = A[i] - A[i - 1]
        if d > x:  # 這段距離太長，需要設路標
            """
                d = 7, x = 3, cnt += 2
                d = 6, x = 3, cnt += 1
                d = 5, x = 3, cnt += 1
            """
            cnt += (d - 1) // x
    return cnt <= K

left, right = 1, L
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        right = mid - 1
    else:
        left = mid + 1
print(left)  # 越大越合法，問最小的合法值