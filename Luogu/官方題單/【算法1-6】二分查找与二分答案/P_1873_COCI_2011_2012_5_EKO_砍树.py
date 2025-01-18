n, m = map(int, input().split())
A = list(map(int, input().split()))

def check(x):
    return sum(a - x for a in A if a > x) >= m

left, right = 0, max(A)
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        left = mid + 1
    else:
        right = mid - 1
print(right)  # 越小越合法，問最大合法值