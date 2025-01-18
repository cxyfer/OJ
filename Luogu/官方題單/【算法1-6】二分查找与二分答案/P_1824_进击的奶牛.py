N, C = map(int, input().split())
A = [int(input()) for _ in range(N)]
A.sort()

def check(x):
    cnt = 0
    last = -float('inf')
    for a in A:
        if a - last >= x:
            cnt += 1
            last = a
    return cnt >= C

left, right = 0, max(A)
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        left = mid + 1
    else:
        right = mid - 1
print(right)  # 越小越合法，問最大合法值