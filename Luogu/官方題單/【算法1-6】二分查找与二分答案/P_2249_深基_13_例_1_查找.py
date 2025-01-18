n, m = map(int, input().split())
A = list(map(int, input().split()))
quries = list(map(int, input().split()))

def find(x):
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left + 1 if left < n and A[left] == x else -1

for i in range(m):
    print(find(quries[i]), end = " ")