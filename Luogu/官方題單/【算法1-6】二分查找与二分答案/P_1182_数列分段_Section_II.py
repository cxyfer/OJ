N, M = map(int, input().split())
A = list(map(int, input().split()))

# 是否可以分出 M 段，每段和 <= x
def check(x):
    cnt = cur = 0
    for a in A:
        if cur + a > x:
            cnt += 1
            cur = a
        else:
            cur += a
    cnt += 1  # 最後一段
    return cnt <= M

left, right = max(A), sum(A)
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        right = mid - 1
    else:
        left = mid + 1
print(left)  # 越大越合法，問最小的合法值