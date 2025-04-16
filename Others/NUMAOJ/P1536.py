"""
【华为】20230412_2_交易系统的降级策略
https://niumacode.com/problem/P1536
"""

A = list(map(int, input().split()))
k = int(input())

if sum(A) <= k:
    exit(print(-1))

def check(m):
    return sum(min(x, m) for x in A) <= k

left, right = 0, max(A)
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        left = mid + 1
    else:
        right = mid - 1
print(right)