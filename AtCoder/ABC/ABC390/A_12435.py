A = list(map(int, input().split()))
n = len(A)
s = sorted(A)

for i in range(n - 1):
    A[i], A[i+1] = A[i+1], A[i]
    if A == s:
        print("Yes")
        break
    A[i], A[i+1] = A[i+1], A[i]
else:
    print("No")