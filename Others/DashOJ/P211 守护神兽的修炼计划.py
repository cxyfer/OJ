import math

n = int(input())
A = list(map(int, input().split()))

K = math.ceil(math.log2(max(A) / A[0]))

ans = float('inf')
for k in range(K + 1):
    a0 = A[0] * (1 << k)

    def check(mid):
        cnt = 0
        for ai in A[1:]:
            while ai > a0:
                ai //= 2
                cnt += 1
        return cnt <= mid

    left, right = 0, 100
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            right = mid - 1
        else:
            left = mid + 1

    ans = min(ans, k + left)

print(ans)