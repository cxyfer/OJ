n = int(input())
A = list(map(int, input().split()))

A.sort()
m = A[n // 2]
print(sum(abs(x - m) for x in A))